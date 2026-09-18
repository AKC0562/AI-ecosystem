from typing import Any, Callable

from core.llm import LLMProvider


class Agent:

    def __init__(
        self,
        name: str,
        instructions: str,
        llm: LLMProvider,
        tools: list[Callable] | None = None,
    ):
        self.name = name
        self.instructions = instructions
        self.llm = llm
        self.tools = tools or []

    def run(self, task: str) -> dict[str, Any]:

        prompt = f"""
You are {self.name}.

Your instructions:
{self.instructions}

User task:
{task}
"""

        response = self.llm.generate(prompt)

        return {
            "agent": self.name,
            "response": response,
            "status": "completed"
        }