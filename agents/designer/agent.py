from core.agent import Agent
from core.llm import MockLLMProvider


closer = Agent(
    name="Client Closer",
    instructions="""
    Communicate with qualified clients,
    answer questions, qualify requirements,
    and schedule meetings for human handoff.
    """,
    llm=MockLLMProvider(),
)