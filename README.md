# AI_Projects

Welcome to **AI_Projects**, a collection of practical AI-powered projects demonstrating skills in FastAPI, Large Language Models (LLMs), RAG pipelines, and data management systems. Each project is self-contained with its own code, README, and documentation.

## 📂 Projects Included

### 1. Student Management API

A simple REST API for managing student records. It allows you to add, view, update, and delete students. All data is stored in-memory, and each student gets a unique ID and timestamp automatically.

**Key Features:**
- CRUD operations for student data
- Unique ID and timestamp generation
- Built with FastAPI and Pydantic
- Fully testable via Swagger UI

**Technologies Used:** FastAPI, Pydantic, Uvicorn, UUID, Datetime

🔗 [View Student Management API README](path_to_student_management_api_readme)

---

### 2. IntelliCourse Advisor

An AI-powered course advisor that helps students make intelligent course decisions using RAG pipelines and LLMs. It can answer queries like prerequisites, course content, or interdisciplinary course suggestions.

**Key Features:**
- Context-aware course recommendations
- Multi-tool AI agent using LangGraph
- Semantic search with ChromaDB + Sentence Transformers
- REST API with FastAPI
- LLM-powered responses via Google Gemini

**Technologies Used:** FastAPI, LangChain, LangGraph, ChromaDB, Google Gemini, Hugging Face Embeddings

🔗 [View IntelliCourse Advisor README](path_to_intelli_course_advisor_readme)

---

## ⚙️ Getting Started

Clone the repository:

```bash
git clone https://github.com/Huxaifa-101/AI_Projects.git
cd AI_Projects
```
Navigate to each project folder and follow their respective setup instructions. Each project has its own virtual environment, dependencies, and run commands.

## 📖 Documentation & Testing
Student Management API: Swagger UI at /docs after running the server.

IntelliCourse Advisor: /chat endpoint for processing student queries with context-aware answers.

## 🚀 Learning Outcomes
By exploring these projects, you will:

Build REST APIs with FastAPI
Implement CRUD operations and data validation
Use RAG pipelines for intelligent retrieval
Integrate LLMs for generating accurate responses
Work with embeddings and vector databases
Design multi-tool AI agents
Happy Coding! This repository demonstrates practical AI and backend skills suitable for portfolios and real-world applications.

