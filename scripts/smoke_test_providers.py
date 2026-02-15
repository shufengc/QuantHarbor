import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.embeddings import EmbeddingClient
from src.core.llm_client import LLMRouter


def main() -> None:
    parser = argparse.ArgumentParser(description="Smoke test provider APIs.")
    parser.add_argument("--provider", type=str, default="auto", choices=["auto", "openai", "deepseek"])
    args = parser.parse_args()

    load_dotenv(PROJECT_ROOT / ".env")
    if args.provider in {"openai", "deepseek"}:
        os.environ["PRIMARY_PROVIDER"] = args.provider
        os.environ["FALLBACK_PROVIDER"] = args.provider

    router = LLMRouter()
    text = router.chat("Respond with: provider test ok", "You are a test assistant.")
    print(f"Chat response: {text[:120]}")

    embedder = EmbeddingClient(provider=os.getenv("PRIMARY_PROVIDER", "openai"))
    vec = embedder.embed_query("provider embedding test")
    print(f"Embedding dimension: {len(vec)}")
    print("Smoke test passed.")


if __name__ == "__main__":
    main()
