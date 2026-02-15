# Migration Notes

This project was rebuilt from a wrapper-style structure into a self-contained implementation.

## What changed

- Removed runtime dependency on external lecture folders.
- Replaced course-style documentation with product-style documentation.
- Added provider abstraction and fallback for OpenAI and DeepSeek.
- Added standalone scripts for ingestion, indexing, pipeline execution, and provider smoke tests.
- Added workspace-wide audit notes for PDFs, ZIP files, and notebooks.
- Standardized secure key handling: real keys only in local `.env`, never in tracked files.

## Deprecated files

The old step scripts and legacy docs were replaced by:
- `scripts/ingest_pdfs.py`
- `scripts/build_index.py`
- `scripts/run_pipeline.py`
- `scripts/smoke_test_providers.py`
- `docs/api_setup_openai_deepseek.md`
- `docs/pdf_coverage_and_ocr.md`

## Upgrade path

1. Recreate environment and reinstall dependencies.
2. Update `.env` based on `.env.example`.
3. Run provider smoke tests.
4. Ingest PDFs and build index.
5. Run query/report pipeline.
