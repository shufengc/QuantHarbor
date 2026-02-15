import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.tools.pdf_ingest import extract_pdf_pages, scan_pdf_files


def parse_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y"}


def load_config() -> Dict[str, Any]:
    with (PROJECT_ROOT / "config" / "project_config.yaml").open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    load_dotenv(PROJECT_ROOT / ".env")
    parser = argparse.ArgumentParser(description="Ingest PDFs into local project data.")
    parser.add_argument("--source-dir", type=str, required=True, help="Directory to scan for PDFs")
    parser.add_argument("--recursive", type=str, default="true", help="true/false")
    args = parser.parse_args()

    config = load_config()
    raw_dir = Path(config["paths"]["raw_pdf_dir"])
    parsed_dir = Path(config["paths"]["parsed_dir"])
    raw_dir.mkdir(parents=True, exist_ok=True)
    parsed_dir.mkdir(parents=True, exist_ok=True)

    src_dir = Path(args.source_dir)
    pdf_files = scan_pdf_files(src_dir, recursive=parse_bool(args.recursive))
    # Avoid re-ingesting already copied files under this project.
    raw_dir_resolved = raw_dir.resolve()
    pdf_files = [p for p in pdf_files if raw_dir_resolved not in p.resolve().parents]
    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found under: {src_dir}")

    all_pages: List[Dict[str, Any]] = []
    for pdf in pdf_files:
        target = raw_dir / pdf.name
        if not target.exists():
            shutil.copy2(pdf, target)
        pages = extract_pdf_pages(target)
        all_pages.extend(pages)

    with (parsed_dir / "pages.json").open("w", encoding="utf-8") as f:
        json.dump(all_pages, f, ensure_ascii=False, indent=2)

    ocr_needed = sum(1 for p in all_pages if p["ocr_required"])
    print(f"Ingested PDFs: {len(pdf_files)}")
    print(f"Extracted pages: {len(all_pages)}")
    print(f"Pages flagged OCR-required: {ocr_needed}")
    print(f"Output: {parsed_dir / 'pages.json'}")


if __name__ == "__main__":
    main()
