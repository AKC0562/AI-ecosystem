from core.agent import Agent
from core.llm import MockLLMProvider


designer = Agent(
    name="Pre-Sales Designer",
    instructions="""
    Create personalized designs,
    prototypes, and pre-sales assets
    for qualified leads.
    """,
    llm=MockLLMProvider(),
)