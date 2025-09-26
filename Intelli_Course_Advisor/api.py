import sys, os
# add "agent" folder to sys.path so imports from it work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'agent')))

from fastapi import FastAPI
from pydantic import BaseModel

# import compiled LangGraph app from agent_graph.py
from agent.agent_graph import app as langgraph_app  # compiled agent

# --- pydantic models ---

class QueryRequest(BaseModel):
    # incoming request body
    query: str

class QueryResponse(BaseModel):
    # outgoing response body
    answer: str
    context: list | None = None      # optional context data from agent
    source_tool: str | None = None   # which tool/chain produced answer

# --- fastapi app instance ---

api = FastAPI(title="Intelli Course Advisor")

@api.post("/chat", response_model=QueryResponse)
async def chat_endpoint(user_input: QueryRequest):
    """
    POST /chat
    accepts a student query and returns the agent's answer,
    optional context, and which tool was used
    """
    # call the LangGraph agent
    result = langgraph_app.invoke(
        {"input": user_input.query},
        config={"configurable": {"thread_id": "api"}}
    )

    # map agent result into response model
    return QueryResponse(
        answer=result.get("answer", ""),
        context=result.get("context", []),
        source_tool=result.get("next", "")
    )

# run API with: uvicorn main:api --reload
