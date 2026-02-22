import re
from pathlib import Path
from typing import Dict, List

from pypdf import PdfReader


def _sanitize_text(text: str) -> str:
    # Remove invalid Unicode surrogate code points that break JSON serialization.
    return re.sub(r"[\uD800-\uDFFF]", "", text)


def extract_pdf_pages(pdf_path: Path) -> List[Dict]:
    reader = PdfReader(str(pdf_path))
    pages: List[Dict] = []
    for idx, page in enumerate(reader.pages, start=1):
        text = _sanitize_text(page.extract_text() or "")
        pages.append(
            {
                "source_file": pdf_path.name,
                "source_path": str(pdf_path),
                "page": idx,
                "text": text.strip(),
                "ocr_required": len(text.strip()) < 40,
            }
        )
    return pages


def scan_pdf_files(source_dir: Path, recursive: bool = True) -> List[Path]:
    if recursive:
        return sorted(source_dir.rglob("*.pdf"))
    return sorted(source_dir.glob("*.pdf"))
