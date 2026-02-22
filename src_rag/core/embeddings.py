import os
from typing import List, Optional

import numpy as np
from openai import OpenAI


class EmbeddingClient:
    def __init__(self, provider: Optional[str] = None) -> None:
        self.provider = (provider or os.getenv("PRIMARY_PROVIDER", "openai")).lower()

    def _build_client(self, provider: str) -> tuple[OpenAI, str]:
        upper = provider.upper()
        api_key = os.getenv(f"{upper}_API_KEY", "")
        base_url = os.getenv(f"{upper}_BASE_URL", "")
        model = os.getenv(f"{upper}_EMBED_MODEL", "")
        if not api_key:
            raise ValueError(f"Missing {upper}_API_KEY.")
        if not model:
            raise ValueError(f"Missing {upper}_EMBED_MODEL.")
        client = OpenAI(api_key=api_key, base_url=base_url or None)
        return client, model

    def embed_texts(self, texts: List[str], batch_size: int = 64) -> np.ndarray:
        preferred = self.provider
        providers = [preferred]
        if preferred != "openai":
            providers.append("openai")

        last_exc: Exception | None = None
        for p in providers:
            try:
                client, model = self._build_client(p)
                vectors: List[List[float]] = []
                for i in range(0, len(texts), batch_size):
                    batch = texts[i : i + batch_size]
                    resp = client.embeddings.create(model=model, input=batch)
                    vectors.extend(item.embedding for item in resp.data)
                return np.array(vectors, dtype=np.float32)
            except Exception as exc:  # noqa: BLE001
                last_exc = exc
        raise RuntimeError(f"Embedding failed for providers {providers}: {last_exc}")

    def embed_query(self, query: str) -> np.ndarray:
        return self.embed_texts([query], batch_size=1)[0]
