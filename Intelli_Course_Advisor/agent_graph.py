import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph
from typing import TypedDict, Literal, List

#  Import your retriever + web search
from tools.course_retriever import get_course_retriever  # your Pinecone wrapper
from tools.web_search import tavily_search

#  Google Gemini LLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# Build retriever + tools

retriever = get_course_retriever(k=20)  # Pinecone retriever
web_search = tavily_search  # already a function

# LLM = Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0,
    google_api_key="AIzaSyBW1yyKiOtIy5QhXNo1ZaGGFrRbKLopPQY"   # 👈 pass key directly
)
# -------------------
#  Prompt Template
# -------------------
generation_prompt = PromptTemplate(
    input_variables=["query", "context"],
    template="""
You are a helpful university assistant. Use the context below to answer the student’s question.

Question:
{query}

Context:
{context}

Instructions:
- For **course-related** questions, answer only from the course catalog context.  
  • State prerequisites clearly if asked (use “The prerequisite is …” or “The prerequisites are …”).  
  • Include both course code and title when possible.  
  • If nothing relevant, reply exactly: "I don’t know".

- For **general knowledge** questions, answer only from the web search context.  
  • Summarize concisely in your own words.  
  • If nothing relevant, reply exactly: "I don’t know".

- Be concise, factual, and do not invent information.
"""
)



# State schema

class AgentState(TypedDict):
    input: str
    context: List[str]
    answer: str
    next: Literal["course", "web"]

graph = StateGraph(AgentState)

# Router node

def router_node(state: AgentState) -> dict:
    question = state["input"]
    return {"next": "course"} if "course" in question.lower() or "hum" in question.lower() else {"next": "web"}

graph.add_node("router", router_node)
graph.set_entry_point("router")

# Course node

def course_node(state: AgentState) -> dict:
    query = state["input"]
    docs = retriever.invoke(query)
    state["context"] = [d.page_content for d in docs]
    return state

graph.add_node("course", course_node)


# Web node

def web_node(state: AgentState) -> dict:
    query = state["input"]
    results = web_search(query)
    if isinstance(results, list):
        state["context"] = [r.get("content", str(r)) for r in results]
    else:
        state["context"] = [str(results)]
    return state

graph.add_node("web", web_node)


# Generation node (Gemini + enhanced prompt)
def generation_node(state: AgentState) -> dict:
    query = state["input"]
    context_text = "\n\n".join(
        doc if isinstance(doc, str) else str(doc)
        for doc in state.get("context", [])
    )

    prompt = generation_prompt.format(query=query, context=context_text)
    response = llm.invoke(prompt)
    state["answer"] = response.content  # store in state["answer"]
    return state

graph.add_node("generate", generation_node)


# Edges
def decide_next(state: AgentState) -> str:
    return state.get("next")

graph.add_conditional_edges(
    "router",
    decide_next,
    {"course": "course", "web": "web"}
)
graph.add_edge("course", "generate")
graph.add_edge("web", "generate")
graph.set_finish_point("generate")

app = graph.compile()

if __name__ == "__main__":
    while True:
        q = input("Ask a question (or 'quit'): ")
        if not q.strip():
            continue
        if q.lower() == "quit":
            break
        result = app.invoke(
            {"input": q},
            config={"configurable": {"thread_id": "session1"}}
        )
        print(result["answer"])
