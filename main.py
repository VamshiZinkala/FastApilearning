print("FILE EXECUTION STARTED")
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
app = FastAPI()

print("LOADED THIS FILE")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contact/{name}")
def contact(name: str , age:Optional[int]=None):
    return {"message": f"contact page {name} and age is {age}"}


class Student(BaseModel):
    name:str
    age:int
    course:str

@app.post("/student")
def create_student(student:Student):
    return{
        "name":student.name,
        "age" :student.age,
        "course":student.course
    }