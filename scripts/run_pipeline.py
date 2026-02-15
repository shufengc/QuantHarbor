import argparse
import json
import sys
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.report_pipeline import ReportPipeline


def main() -> None:
    load_dotenv(PROJECT_ROOT / ".env")
    parser = argparse.ArgumentParser(description="Run integrated report pipeline.")
    parser.add_argument("--question", type=str, required=True)
    parser.add_argument("--top-k", type=int, default=0)
    args = parser.parse_args()

    pipeline = ReportPipeline(PROJECT_ROOT / "config" / "project_config.yaml")
    result = pipeline.run(args.question, top_k=args.top_k or None)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
