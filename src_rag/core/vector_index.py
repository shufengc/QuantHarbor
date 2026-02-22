import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import numpy as np


def chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
    if not text.strip():
        return []
    chunks: List[str] = []
    start = 0
    step = max(1, chunk_size - chunk_overlap)
    while start < len(text):
        end = start + chunk_size
        part = text[start:end].strip()
        if part:
            chunks.append(part)
        start += step
    return chunks


@dataclass
class RetrievedChunk:
    content: str
    source_file: str
    page: int
    score: float


class VectorIndex:
    def __init__(self, index_dir: Path) -> None:
        self.index_dir = index_dir
        self.meta_file = index_dir / "metadata.json"
        self.emb_file = index_dir / "embeddings.npy"

    def save(self, metadata: List[Dict], embeddings: np.ndarray) -> None:
        self.index_dir.mkdir(parents=True, exist_ok=True)
        with self.meta_file.open("w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        np.save(self.emb_file, embeddings)

    def load(self) -> tuple[List[Dict], np.ndarray]:
        with self.meta_file.open("r", encoding="utf-8") as f:
            metadata = json.load(f)
        embeddings = np.load(self.emb_file)
        return metadata, embeddings

    @staticmethod
    def search(query_vec: np.ndarray, embeddings: np.ndarray, top_k: int) -> np.ndarray:
        # Sanitize vectors to avoid overflow/NaN propagation from noisy inputs.
        emb64 = np.nan_to_num(np.asarray(embeddings, dtype=np.float64), nan=0.0, posinf=0.0, neginf=0.0)
        q64 = np.nan_to_num(np.asarray(query_vec, dtype=np.float64), nan=0.0, posinf=0.0, neginf=0.0)
        emb64 = np.clip(emb64, -1e6, 1e6)
        q64 = np.clip(q64, -1e6, 1e6)

        # Row-wise stable normalization.
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            emb_norm = np.linalg.norm(emb64, axis=1)
            q_norm = np.linalg.norm(q64)
        valid_rows = np.isfinite(emb_norm) & (emb_norm > 1e-12)
        emb_unit = np.zeros_like(emb64)
        emb_unit[valid_rows] = emb64[valid_rows] / emb_norm[valid_rows, None]

        if not np.isfinite(q_norm) or q_norm <= 1e-12:
            sims = np.full((emb64.shape[0],), -1.0, dtype=np.float64)
            return np.argsort(sims)[::-1][:top_k], sims

        q_unit = q64 / q_norm
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            sims = emb_unit @ q_unit
        sims = np.nan_to_num(sims, nan=-1.0, posinf=-1.0, neginf=-1.0)
        return np.argsort(sims)[::-1][:top_k], sims
