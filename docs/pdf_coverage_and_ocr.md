# PDF Coverage and OCR Status

This project reviewed inventory coverage for PDF sources in your `Quant` workspace.

## Identified PDFs

Total currently identified in workspace: 138.

- Lecture-group coverage:
  - Group 1: 3 PDFs
  - Group 2: 129 PDFs (including the large financial report corpus)
  - Group 3: 2 PDFs
  - Group 4: 0 PDFs
  - Group 5: 1 PDF
  - Group 6: 0 PDFs
  - Group 7: 0 PDFs
  - Group 8: 3 PDFs

To keep this project English-only, this file does not repeat non-English source file names.
The ingestion script scans source folders directly and records exact file paths in local artifacts.

## ZIP Audit

- No `.zip` files are currently present anywhere under `Quant`.
- The previously mentioned report database archive appears already extracted.

## Notebook Audit

- Total notebooks discovered: 13.
- Core-aligned for this product pipeline: 2 (offline/online RAG workflow notebooks).
- Optional or experimental for this product: 11.

## Extraction Status

- Some PDFs expose extractable text directly.
- Some are image-based or partially image-based; plain extraction returns sparse content.
- OCR is required for complete and reliable extraction on image-heavy files.

## Recommended OCR Workflow

1. Run OCR on image-based PDFs using one of:
   - Adobe Acrobat OCR
   - Tesseract OCR
   - PaddleOCR
2. Save OCR outputs into:
   - `data/ocr_text/` (plain text or markdown)
3. Use `scripts/ingest_pdfs.py` to include OCR text and/or extracted PDF text.

## Integration Note

- The production pipeline in this folder can operate with mixed sources:
  - directly extractable PDFs
  - OCR-generated text files for low-extraction PDFs
