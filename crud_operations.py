from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

Students = [
    {"id": 1, "name": "Vamshi", "class_": "CSE"},
    {"id": 2, "name": "Ananya", "class_": "ECE"},
    {"id": 3, "name": "Rahul", "class_": "MECH"},
    {"id": 4, "name": "Priya", "class_": "EEE"},
    {"id": 5, "name": "Suresh", "class_": "CIVIL"}
]

@app.get("/students")
def get_students():
    return Students

@app.get("/students/{id}")
def get_student(id: int):
    for student in Students:
        if student["id"] == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


class Student(BaseModel):
    id:int
    name :str
    class_:str

@app.post("/student")
def create_student(student:Student):
    new_student =student.model_dump()
    Students.append(new_student)
    return new_student
 

class StudentUpdate(BaseModel):
    name:str
    class_:str

@app.put("/student/{student_id}")
def update_student(student_id:int,student_update:StudentUpdate):
    for student in Students:
        if student["id"] == student_id:
            student["name"] =student_update.name
            student["class_"] =student_update.class_
            return student
    raise HTTPException(status_code=404, detail="Student not found")   

@app.delete("/student/{student_id}")
def delete_student(student_id:int):
    for student in Students:
        if student["id"] == student_id:
            Students.remove(student)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")