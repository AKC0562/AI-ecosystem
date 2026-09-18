from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentStart(TypedDict):
    task: str
    response: str

def agent_node(state: AgentStart):
    task = state["task"]

    return{
        "response": f"Agent received task: {task}. Processing..."
    }

builder = StateGraph(AgentStart)

builder.add_node("agent", agent_node)

builder.add_edge(START, "agent")
builder.add_edge("agent", END)

agent_graph = builder.compile()