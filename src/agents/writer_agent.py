from typing import Any, Dict, List

from src.core.llm_client import LLMRouter


class WriterAgent:
    def __init__(self) -> None:
        self.router = LLMRouter()

    def write(self, question: str, analysis: str, retrieved: List[Dict[str, Any]]) -> str:
        citations = [
            f"- {item['source_file']} (page {item['page']}, score {item['score']:.4f})"
            for item in retrieved
        ]
        prompt = (
            "Write a final concise report answer in English.\n"
            "Structure: Executive Summary, Key Evidence, Risks, Opportunities, Conclusion.\n"
            "Only include claims supported by the analysis/evidence.\n"
            "Avoid generic market commentary not grounded in evidence.\n"
            "When support is weak, label the point as low-confidence.\n"
            "Append source citations at the end.\n\n"
            f"Question: {question}\n\n"
            f"Analysis:\n{analysis}\n\n"
            f"Citations:\n{chr(10).join(citations)}"
        )
        return self.router.chat(prompt, system_prompt="You are a financial report writer.")
