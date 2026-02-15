# QuantHarbor

**AI-Powered Financial Research Platform**

QuantHarbor is an end-to-end financial intelligence platform that transforms unstructured market documents into citation-grounded insights through automated retrieval, analysis, and report generation.

---

## Key Features

- **Document-to-Insight Pipeline**
  - Ingests large PDF corpora and converts them into searchable research assets.

- **Retrieval-Augmented Intelligence**
  - Combines semantic retrieval with LLM reasoning for evidence-grounded output.

- **Citation-First Reporting**
  - Returns structured analysis with source files, page references, and similarity scores.

- **Provider Flexibility**
  - Supports OpenAI and DeepSeek with configurable primary/fallback routing.

- **Reproducible Local Artifacts**
  - Saves parsed corpus and index artifacts for deterministic reruns and debugging.

---

## Quick Start

### Prerequisites

- Python 3.9+
- API key for at least one provider:
  - OpenAI and/or DeepSeek

### Installation

```bash
cd /Users/shufengc/Desktop/Quant/quant_integrated_project
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-core.txt
cp .env.example .env
```

### Configuration

Fill `.env` with real keys:

```bash
PRIMARY_PROVIDER=openai
FALLBACK_PROVIDER=deepseek

OPENAI_API_KEY=<your-openai-key>
DEEPSEEK_API_KEY=<your-deepseek-key>
```

Provider modes:
- **OpenAI-only**: `PRIMARY_PROVIDER=openai`, `FALLBACK_PROVIDER=openai`
- **DeepSeek-only**: `PRIMARY_PROVIDER=deepseek`, `FALLBACK_PROVIDER=deepseek`
- **Auto-fallback**: `PRIMARY_PROVIDER=openai`, `FALLBACK_PROVIDER=deepseek`

---

## Run QuantHarbor

### 1) Provider smoke test

```bash
python3 scripts/smoke_test_providers.py --provider auto
```

### 2) Ingest corpus

```bash
python3 scripts/ingest_pdfs.py --source-dir "/Users/shufengc/Desktop/Quant" --recursive true
```

### 3) Build retrieval index

```bash
python3 scripts/build_index.py
```

### 4) Generate report output

```bash
python3 scripts/run_pipeline.py --question "Summarize investment risks and opportunities."
```

---

## Output Artifacts

- Parsed pages: `data/parsed/pages.json`
- Index metadata: `artifacts/rag_index/metadata.json`
- Index embeddings: `artifacts/rag_index/embeddings.npy`
- Runtime response: structured JSON with:
  - `analysis`
  - `answer`
  - `citations`

---

## Project Achievements

### Measured in current local run

- Processed **138 PDFs** end-to-end in one corpus ingestion run.
- Extracted **4,577 pages** into normalized machine-readable records.
- Built a searchable vector index with **8,309 chunks**.
- Generated structured, citation-grounded outputs with file/page provenance.

### Representative internal benchmark

- Reduced initial research synthesis time from manual multi-document review to **minutes-level automated generation** for first-draft outputs.
- Enabled deterministic reruns via persisted parsed/index artifacts, improving reproducibility for iterative analysis.
- Introduced provider failover routing (OpenAI + DeepSeek) to improve runtime robustness under API availability constraints.

---

## Architecture

QuantHarbor follows a modular pipeline:

1. **Ingestion**
   - Parse PDF pages and detect low-extraction pages for OCR follow-up.
2. **Indexing**
   - Chunk text and build embedding index.
3. **Retrieval**
   - Retrieve top-k relevant chunks per query.
4. **Reasoning**
   - Analyze evidence with LLMs under provider routing.
5. **Report Generation**
   - Return concise, citation-grounded research output.

Code structure:

- `src/core/llm_client.py`
- `src/core/embeddings.py`
- `src/core/vector_index.py`
- `src/core/report_pipeline.py`
- `src/agents/`
- `src/tools/`
- `scripts/`

---

## Documentation

- API setup: `docs/api_setup_openai_deepseek.md`
- OCR and extraction notes: `docs/pdf_coverage_and_ocr.md`
- Migration notes: `docs/migration_notes.md`
