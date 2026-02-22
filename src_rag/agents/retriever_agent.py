from pathlib import Path
from typing import Any, Dict, List
import math

from src.core.embeddings import EmbeddingClient
from src.core.vector_index import VectorIndex


class RetrieverAgent:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config
        self.index = VectorIndex(Path(config["artifacts"]["rag_index_dir"]))
        self.embedder = EmbeddingClient()

    def retrieve(self, question: str, top_k: int) -> List[Dict[str, Any]]:
        metadata, embeddings = self.index.load()
        query_vec = self.embedder.embed_query(question)
        idxs, sims = self.index.search(query_vec, embeddings, top_k=top_k)
        results: List[Dict[str, Any]] = []
        for i in idxs:
            score = float(sims[int(i)])
            if not math.isfinite(score):
                continue
            item = metadata[int(i)]
            results.append(
                {
                    "content": item["content"],
                    "source_file": item["source_file"],
                    "page": item["page"],
                    "score": score,
                }
            )
        # Keep ordering stable and drop clearly irrelevant negative similarities.
        results = [r for r in results if r["score"] > 0]
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]
