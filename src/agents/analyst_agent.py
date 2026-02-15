from typing import Any, Dict, List

from src.core.llm_client import LLMRouter


class AnalystAgent:
    def __init__(self) -> None:
        self.router = LLMRouter()

    def analyze(self, question: str, retrieved: List[Dict[str, Any]]) -> str:
        snippets = []
        for item in retrieved:
            snippets.append(
                f"file={item['source_file']} page={item['page']} score={item['score']:.4f}\n"
                f"{item['content'][:1500]}"
            )
        prompt = (
            "Analyze only the retrieved evidence and extract key facts, risks, and opportunities.\n"
            "Do not fabricate facts outside the evidence.\n"
            "If evidence is weak for a claim, mark it as low-confidence.\n"
            "Use concise bullet points and keep claims directly grounded in the provided snippets.\n\n"
            f"Question: {question}\n\n"
            f"Evidence:\n{chr(10).join(snippets)}"
        )
        return self.router.chat(prompt, system_prompt="You are a rigorous financial analyst.")
