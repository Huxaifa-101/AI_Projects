# 📚 Intelli Course Advisor

## 🚀 Project Vision

Imagine being a student trying to decide which courses to take next semester. You may ask:

- "What are the prerequisites for the advanced machine learning course?"  
- "Which courses cover Python and data visualization?"  
- "Give me a course that combines biology with computer science."  

**IntelliCourse** saves you from searching through long  documents by providing clear, accurate, and relevant answers. Using a Retrieval-Augmented Generation (RAG) pipeline, this AI assistant, built as a REST API, demonstrates skills in AI, Large Language Models (LLMs), and smart information retrieval.**

---

## 🌟 Key Features

- Context-aware course recommendations using a **RAG pipeline**.  
- Multi-tool AI agent with **LangGraph**: combines course data and live web search.  
- FastAPI-based REST API for easy integration.  
- Semantic search using **ChromaDB + Sentence Transformers**.  
- LLM integration with **Google Gemini** for high-quality responses.  

---

## 🎯 Learning Objectives

By completing this project, you will:

- Build a robust **REST API** using Python & FastAPI.  
- Implement **RAG pipelines** for querying a custom knowledge base.  
- Utilize **LLMs** (Google Gemini) and embedding models (Hugging Face).  
- Design a **multi-tool agent** using LangGraph.  
- Gain hands-on experience with `langchain`, `langgraph`, `fastapi`, and **ChromaDB**.  

---

## 🛠️ Core Technologies

| Category            | Technology / Tool |
|--------------------|-----------------|
| API Framework       | FastAPI          |
| LLM Orchestration   | LangChain & LangGraph |
| LLM                 | Google Gemini (via `langchain-google-genai`) |
| Embedding Model     | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Database     | ChromaDB         |

---

## 📂 File Descriptions

| File | Description |
|------|------------|
| `index_documents.py` | Indexes course `.docx` files: splits into chunks, embeds them, stores in ChromaDB. |
| `retriever_test.py` | Demonstrates initializing Chroma vector store and retrieving documents. |
| `course_retriever.py` | Returns a retriever object to fetch course info based on queries. |
| `web_search.py` | Integrates Tavily web search for general queries. |
| `agent_graph.py` | LangGraph agent logic: **Router Node**, **Course Node**, **Web Node**, **Generation Node**. |
| `api.py` | FastAPI application: defines `/chat` endpoint for processing student queries. |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Huxaifa-101/AI_Projects.git
cd AI_Projects/Intelli_Course_Advisor
```
### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate # On Linux/Mac
venv\Scripts\activate # On Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Setup Environment Variables
To run this project, you will need to add the following environment variables to your .env file

# API Keys

- `GOOGLE_API_KEY`=your_google_api_key
- `TAVILY_API_KEY`=your_tavily_api_key

# Vector DB + Embeddings

- `HUGGINGFACE_EMBEDDING_MODEL`=sentence-transformers/all-MiniLM-L6-v2

### 5. Run FastAPI Server
```bash
uvicorn app.api:api_app --reload
```
Server will start at: http://127.0.0.1:8000/

---
## 📡 API Documentation

- **Endpoint**: /chat
- **Method**: POST
- **Description**: Takes a student query and returns an intelligent answer.
- **Request Body**: {"query": "What are the prerequisites for Software Engineering?"}


#### Response Body Example

| Field        | Description                                        | Example                               |
|--------------|----------------------------------------------------|---------------------------------------|
| `answer`     | The agent's generated response.                    | `"The prerequisite is ENG 101."`     |
| `context`    | The text chunks or search results used.            | `["...", "..."]`                      |
| `source_tool`| Indicates which tool was used: `course` or `web`. | `"course"`                            |

```json
{
  "answer": "Paris is the capital and most populous city of France.",
  "context": [
    "Paris: https://en.wikipedia.org/wiki/Paris"
  ],
  "source_tool": "web"
}
```


Thank you for engaging with the **IntelliCourse Advisor** project! Happy coding!
```
