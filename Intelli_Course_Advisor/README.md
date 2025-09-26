
# 📚 Intelli Course Advisor

## Project Vision 🚀

Imagine you're a student trying to determine which courses to take next semester. You may have questions like:
- "What are the prerequisites for the advanced machine learning course?"
- "Which courses cover Python and data visualization?"
- "Give me a course that combines biology with computer science."

Sifting through dense PDF catalogs is tedious. Your task is to build **IntelliCourse**, a REST API-powered AI assistant that intelligently answers these questions. This project showcases your skills in modern AI engineering, including API development, Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG).

## Learning Objectives

Upon successful completion of this assignment, you will be able to:
- Develop a robust REST API using Python and FastAPI.
- Implement a Retrieval-Augmented Generation (RAG) pipeline to answer questions from a custom knowledge base.
- Utilize powerful LLMs (like Google's Gemini) and embedding models (from Hugging Face).
- Design and implement a multi-tool agent using LangGraph.
- Gain practical experience with key libraries in the AI ecosystem: `langchain`, `langgraph`, `fastapi`, and ChromaDB.

## Core Technologies

You are required to use the following stack:
- **API Framework**: FastAPI
- **LLM Orchestration**: LangChain & LangGraph
- **LLM**: Google Gemini (via `langchain-google-genai`)
- **Embedding Model**: Sentence Transformers (using `all-MiniLM-L6-v2`)
- **Vector Database**: ChromaDB for storing your embeddings.

## File Descriptions
### 1. `index_documents.py`

This script handles the indexing of course documents:
- Loads `.docx` files from the `data/raw` directory.
- Splits the documents into manageable chunks.
- Embeds these chunks and stores them in ChromaDB.

### 2. `retriever_test.py`

This script showcases how to initialize the Chroma vector store and retrieve relevant documents:
- Loads the embeddings model.
- Converts the Chroma vector store into a retriever.
- Examples of queries to test the retriever's functionality.

### 3. `course_retriever.py`

This file provides a function to create a retriever for the course catalog:
- Loads the existing Chroma database and initializes the embeddings model.
- Returns a retriever object that can fetch relevant course information based on queries.

### 4.`web_search.py`

This module integrates the Tavily web search:
- Initializes the Tavily client with the API key.
- Contains a function to perform web searches and return formatted results.

### 5.. `agent_graph.py`

This file defines the agent's logic using LangGraph. It includes:
- **Router Node**: Determines whether a query is course-related or general knowledge.
- **Course Node**: Uses the course retriever to fetch relevant course information.
- **Web Node**: Utilizes the Tavily web search for general queries.
- **Generation Node**: Formats the final response using the LLM.


### 6.`api.py`

This file sets up the FastAPI application:
- Defines Pydantic models for request and response bodies.
- Implements the `/chat` endpoint where user queries are processed by the agent.

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MHS-007/IntelliCourse.git
cd IntelliCourse
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

- `PINECONE_INDEX`=intellicourse-index
- `HUGGINGFACE_EMBEDDING_MODEL`=sentence-transformers/all-MiniLM-L6-v2

### 5. Run FastAPI Server
```bash
uvicorn app.api:api_app --reload
```
Server will start at: http://127.0.0.1:8000

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

## Submission Guidelines

Submit a link to your GitHub repository containing:
- All Python source code organized logically.
- A `requirements.txt` file.
- A detailed `README.md` file as outlined above.

## Evaluation Criteria

- **Functionality (60%)**: Successful retrieval of relevant course information and correct routing of queries.
- **Code Quality (35%)**: Clean, well-commented code that follows Python best practices (PEP 8).
- **Documentation (5%)**: A clear and comprehensive `README.md`.

---

Thank you for engaging with the **IntelliCourse Advisor** project! Happy coding!
```

### Key Features of This `README.md`:
- **Comprehensive Overview**: Clearly articulates the project vision and objectives.
- **Detailed File Descriptions**: Explains the purpose and functionality of each Python file.
- **Setup Instructions**: Provides step-by-step instructions for setting up the project.
- **API Documentation**: Includes examples for using the API endpoint.
- **Submission Guidelines**: Clarifies how to submit the project. 

Feel free to adjust any section to better match your project specifics or personal style!

