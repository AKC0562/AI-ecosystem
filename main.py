from fastapi import FastAPI

from agents.hunter.agent import hunter
from agents.designer.agent import designer
from agents.closer.agent import closer

from core.graph import agent_graph

app = FastAPI(
    title="Ai Ecosystem",
    version="1.0.0"
)

@app.get("/")
def root():
    return{
        "name":"Ai ecosystem",
        "status":"online",
        "agents":[
            "hunter",
            "designer",
            "closer"
        ]
    }

@app.get("/agents")
def get_agents():
    return{
        "agents":[
            {
                "name": hunter.name,
                "status": "ready"
            },
            {
                "name": designer.name,
                "status": "ready"
            },
            {
                "name": closer.name,
                "status": "ready"
            }
        ]
    }

@app.post("/agents/{agent_name}/run")
def run_agent(agent_name: str, task: str):
    agents = {
        "hunter": hunter,
        "designer": designer,
        "closer": closer
    }
    agent = agents.get(agent_name)
    if not agent:
        return {
            "error": "Agent not found"
        }
    return agent.run(task)

@app.post("/test-agent")
def test_agent(task: str):
    result = agent_graph.invoke({
        "task": task,
        "response": ""
    })
    return result