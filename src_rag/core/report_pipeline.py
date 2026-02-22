from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from src.agents.analyst_agent import AnalystAgent
from src.agents.retriever_agent import RetrieverAgent
from src.agents.writer_agent import WriterAgent


class ReportPipeline:
    def __init__(self, config_path: Path) -> None:
        with config_path.open("r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
        self.retriever = RetrieverAgent(self.config)
        self.analyst = AnalystAgent()
        self.writer = WriterAgent()

    def run(self, question: str, top_k: Optional[int] = None) -> Dict[str, Any]:
        top_k_value = top_k or int(self.config["artifacts"]["retrieval_top_k"])
        retrieved = self.retriever.retrieve(question, top_k=top_k_value)
        analysis = self.analyst.analyze(question, retrieved)
        final_text = self.writer.write(question, analysis, retrieved)
        citations: List[Dict[str, Any]] = [
            {
                "source_file": item["source_file"],
                "page": item["page"],
                "score": round(float(item["score"]), 6),
            }
            for item in retrieved
        ]
        return {
            "question": question,
            "analysis": analysis,
            "answer": final_text,
            "citations": citations,
        }
