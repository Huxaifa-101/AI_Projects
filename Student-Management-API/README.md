# Student Management API

This is a simple project made using **FastAPI**. It works like a small student record system where you can add, view, update, and delete students. Instead of using a database, all data is stored in a Python list (in memory). Each student gets a **unique ID** and a **timestamp** when they are added.

---

## ✅ How It Works (API Endpoints)

- **Get All Students** → `GET /students` → Shows all students in the system.  
- **Get Student by ID** → `GET /students/{id}` → Finds one student using their ID.  
- **Add Student** → `POST /students` → Creates a new student. The system automatically gives an ID and created time.  
- **Update Student** → `PUT /students/{id}` → Updates the details of a student but keeps the same ID.  
- **Delete Student** → `DELETE /students/{id}` → Removes a student from the list.  

---

## ⚙️ Tools Used
- **FastAPI** → To build the API.  
- **Uvicorn** → To run the server (`uvicorn main:app --reload`).  
- **Pydantic** → To check and validate student details (like name, age, email).  
- **UUID & Datetime** → To create unique IDs and timestamps.  

---

## 📖 Testing
FastAPI automatically gives API documentation where you can test all functions:

- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
