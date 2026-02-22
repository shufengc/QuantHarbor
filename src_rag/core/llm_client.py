import os
from dataclasses import dataclass
from typing import Optional

from openai import OpenAI


@dataclass
class ProviderConfig:
    name: str
    api_key: str
    base_url: str
    chat_model: str
    embed_model: str


def _provider_from_env(name: str) -> ProviderConfig:
    upper = name.upper()
    api_key = os.getenv(f"{upper}_API_KEY", "")
    base_url = os.getenv(f"{upper}_BASE_URL", "")
    chat_model = os.getenv(f"{upper}_CHAT_MODEL", "")
    embed_model = os.getenv(f"{upper}_EMBED_MODEL", "")
    return ProviderConfig(
        name=name,
        api_key=api_key,
        base_url=base_url,
        chat_model=chat_model,
        embed_model=embed_model,
    )


class LLMRouter:
    def __init__(self, primary: Optional[str] = None, fallback: Optional[str] = None) -> None:
        self.primary_name = (primary or os.getenv("PRIMARY_PROVIDER", "openai")).lower()
        self.fallback_name = (fallback or os.getenv("FALLBACK_PROVIDER", "deepseek")).lower()
        self.primary = _provider_from_env(self.primary_name)
        self.fallback = _provider_from_env(self.fallback_name)

    @staticmethod
    def _client(cfg: ProviderConfig) -> OpenAI:
        if not cfg.api_key:
            raise ValueError(f"Missing {cfg.name.upper()}_API_KEY.")
        return OpenAI(api_key=cfg.api_key, base_url=cfg.base_url or None)

    def _chat_once(self, cfg: ProviderConfig, prompt: str, system_prompt: str) -> str:
        if not cfg.chat_model:
            raise ValueError(f"Missing {cfg.name.upper()}_CHAT_MODEL.")
        client = self._client(cfg)
        resp = client.chat.completions.create(
            model=cfg.chat_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=1200,
        )
        return (resp.choices[0].message.content or "").strip()

    def chat(self, prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
        try:
            return self._chat_once(self.primary, prompt, system_prompt)
        except Exception:
            if self.fallback_name == self.primary_name:
                raise
            return self._chat_once(self.fallback, prompt, system_prompt)
