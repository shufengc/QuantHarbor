import json
import sys
from pathlib import Path
from typing import Any, Dict, List

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.embeddings import EmbeddingClient
from src.core.vector_index import VectorIndex, chunk_text


def load_config() -> Dict[str, Any]:
    with (PROJECT_ROOT / "config" / "project_config.yaml").open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    load_dotenv(PROJECT_ROOT / ".env")
    config = load_config()
    parsed_file = Path(config["paths"]["parsed_dir"]) / "pages.json"
    if not parsed_file.exists():
        raise FileNotFoundError("Missing parsed pages. Run scripts/ingest_pdfs.py first.")

    with parsed_file.open("r", encoding="utf-8") as f:
        pages: List[Dict[str, Any]] = json.load(f)

    chunk_size = int(config["artifacts"]["chunk_size"])
    chunk_overlap = int(config["artifacts"]["chunk_overlap"])
    metadata: List[Dict[str, Any]] = []
    texts: List[str] = []
    for page in pages:
        chunks = chunk_text(page.get("text", ""), chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        for content in chunks:
            metadata.append(
                {
                    "source_file": page["source_file"],
                    "source_path": page["source_path"],
                    "page": page["page"],
                    "content": content,
                }
            )
            texts.append(content)

    if not texts:
        raise ValueError("No extractable text chunks found. OCR may be required.")

    embedder = EmbeddingClient()
    embeddings = embedder.embed_texts(texts)

    index = VectorIndex(Path(config["artifacts"]["rag_index_dir"]))
    index.save(metadata, embeddings)
    print(f"Saved chunks: {len(metadata)}")
    print(f"Saved index: {config['artifacts']['rag_index_dir']}")


if __name__ == "__main__":
    main()
