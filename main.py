from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uuid
from datetime import datetime

app = FastAPI()

# Student model with validation
class Student(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    email: str
    created_at: datetime

# In-memory list to store students
students: List[Student] = []

# Welcome message
@app.get("/")
def home():
    return {"message": "Welcome to the Student API!"}

# Get all students
@app.get("/students", response_model=List[Student])
def get_students():
    return students

# Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: str):
    for student in students:
        if student.id == student_id:
            return student
    return {"error": "Student not found"}, 404

# Add a new student
@app.post("/students", response_model=Student)
def add_student(student: Student):
    student.id = str(uuid.uuid4())  # Generate a unique ID
    student.created_at = datetime.now()  # Set creation timestamp
    students.append(student)
    return student

# Update a student
@app.put("/students/{student_id}")
def update_student(student_id: str, updated_student: Student):
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = updated_student
            students[i].id = student_id  # Keep the same ID
            return students[i]
    return {"error": "Student not found"}, 404

# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    for i, student in enumerate(students):
        if student.id == student_id:
            deleted = students.pop(i)
            return {"message": "Student deleted successfully", "student": deleted}
    return {"error": "Student not found"}, 404