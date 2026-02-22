import json
import os
from typing import List

import requests


def serper_search(query: str, top_k: int = 5) -> List[dict]:
    api_key = os.getenv("SERPER_API_KEY", "")
    if not api_key:
        raise ValueError("Missing SERPER_API_KEY.")
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
    payload = json.dumps({"q": query})
    resp = requests.post(url, headers=headers, data=payload, timeout=30)
    resp.raise_for_status()
    organic = resp.json().get("organic", [])
    return organic[:top_k]
