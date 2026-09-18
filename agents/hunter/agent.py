from core.agent import Agent
from core.llm import MockLLMProvider


hunter = Agent(
    name="Lead Hunter",
    instructions="""
    Find and research potential clients
    who may need websites, software,
    or digital marketing services.
    """,
    llm=MockLLMProvider(),
)