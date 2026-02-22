from src.core.llm_client import LLMRouter


class PlannerAgent:
    def __init__(self) -> None:
        self.router = LLMRouter()

    def plan(self, question: str) -> str:
        prompt = (
            "Create a concise analysis plan for this financial research question.\n"
            "Focus on data needs, key risks, and output structure.\n\n"
            f"Question: {question}"
        )
        return self.router.chat(prompt, system_prompt="You are a financial research planner.")
