# Quant Integrated AI Research Platform

Quant Integrated AI Research Platform is a self-contained document intelligence system for financial research workflows.
It ingests PDF corpora, builds a retrieval index, and generates citation-grounded analytical outputs.

## Core Capabilities

- PDF ingestion with extraction quality checks
- Text chunking and embedding-based indexing
- Retrieval-augmented analysis and report generation
- Provider routing with OpenAI and DeepSeek support
- Deterministic local artifacts for reproducible runs

## Architecture

- `src/core/llm_client.py`: LLM provider abstraction and fallback routing
- `src/core/embeddings.py`: embedding client and provider selection
- `src/core/vector_index.py`: chunking, indexing, similarity search
- `src/core/report_pipeline.py`: retrieval -> analysis -> writing orchestration
- `src/agents/`: retrieval, analysis, and writing agents
- `src/tools/`: PDF ingestion and optional web search utilities

## Setup

```bash
cd /Users/shufengc/Desktop/Quant/quant_integrated_project
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-core.txt
cp .env.example .env
```

Configure `.env` with valid API keys:

```bash
PRIMARY_PROVIDER=openai
FALLBACK_PROVIDER=deepseek
OPENAI_API_KEY=<your-openai-key>
DEEPSEEK_API_KEY=<your-deepseek-key>
```

## Provider Modes

- OpenAI only:
  - `PRIMARY_PROVIDER=openai`
  - `FALLBACK_PROVIDER=openai`
- DeepSeek only:
  - `PRIMARY_PROVIDER=deepseek`
  - `FALLBACK_PROVIDER=deepseek`
- Auto fallback:
  - `PRIMARY_PROVIDER=openai`
  - `FALLBACK_PROVIDER=deepseek`

## End-to-End Run

1) Validate provider connectivity:

```bash
python3 scripts/smoke_test_providers.py --provider auto
```

2) Ingest PDF corpus:

```bash
python3 scripts/ingest_pdfs.py --source-dir "/Users/shufengc/Desktop/Quant" --recursive true
```

3) Build vector index:

```bash
python3 scripts/build_index.py
```

4) Generate analysis output:

```bash
python3 scripts/run_pipeline.py --question "Summarize investment risks and opportunities."
```

## Output Artifacts

- Parsed corpus: `data/parsed/pages.json`
- Index metadata: `artifacts/rag_index/metadata.json`
- Index embeddings: `artifacts/rag_index/embeddings.npy`
- Runtime output: structured JSON response with `analysis`, `answer`, and `citations`

## Documentation

- API setup: `docs/api_setup_openai_deepseek.md`
- Extraction/OCR notes: `docs/pdf_coverage_and_ocr.md`
- Migration notes: `docs/migration_notes.md`
