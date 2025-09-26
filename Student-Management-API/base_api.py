# ----- Libraries -----
from fastapi import FastAPI, HTTPException  # FastAPI framework + HTTP error handling
from pydantic import BaseModel               # Data validation/modeling
from typing import List                      # Type hinting for lists

# ----- FastAPI app instance -----
app = FastAPI()

# ----- Data model -----
class Student(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    email: str

# ----- Dummy data -----
students: List[Student] = [
    Student(id=3, name="Charlie", age=20, gender="Male", email="charlie@example.com")
]

# Track next ID for new students
next_id = len(students) + 1

# ----- Routes -----

@app.get("/")
def home():
    # GET request to root: welcome message
    return {"message": "Welcome to the Student API!"}

@app.get("/students", response_model=List[Student])
def get_students():
    # GET request: return all students
    return students

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    # GET request: return a single student by ID
    for student in students:
        if student.id == student_id:
            return student
    # Raise 404 if student not found
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students", response_model=Student)
def add_student(student: Student):
    # POST request: add a new student
    global next_id
    new_student = Student(id=next_id, **student.dict(exclude={"id"}))
    students.append(new_student)
    next_id += 1
    return new_student

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    # PUT request: update an existing student by ID
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = Student(id=student_id, **updated_student.dict(exclude={"id"}))
            return students[i]
    # Raise 404 if student not found
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    # DELETE request: remove a student by ID
    for i, student in enumerate(students):
        if student.id == student_id:
            deleted = students.pop(i)
            return {"message": "Student deleted successfully", "student": deleted}
    # Raise 404 if student not found
    raise HTTPException(status_code=404, detail="Student not found")
