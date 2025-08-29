# AI_Projects

This project is a Student Management API built using FastAPI.
It demonstrates basic CRUD operations (Create, Read, Update, Delete) on student records stored in a simple Python list (no database).

✅ Features

Get Students → /students (GET) → returns all students

Get Student by ID → /students/{id} (GET) → returns a single student

Add Student → /students (POST) → adds a new student

Update Student → /students/{id} (PUT) → updates student details

Delete Student → /students/{id} (DELETE) → removes a student

⚙️ Tools Used

FastAPI → API framework

Uvicorn → Server to run FastAPI

Pydantic → Data validation for student fields (name, age, gender, email)

📖 Testing

You can test the API with:

Swagger UI (auto-generated docs at http://127.0.0.1:8000/docs)
