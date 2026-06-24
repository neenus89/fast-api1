from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from schemas import Student
from schemas import StudentResponse
from schemas import UserRegister

app = FastAPI()

@app.get("/")
def read_root():
    return {"data" : {"name" : "Hello World"}}

@app.get("/about")
def about():
    return {"data" : {"name" : "This is the about page"}}

@app.get("/show/{id}")
def show(id: int):
    return {"data" : {"id" : id}}

@app.get("/show/{id}/comments")
def show_comments(id: int):
    return {"data" : {"1", "2", "3"}}

# Assignment 1

@app.get("/books/search")
def search(author : str, year : int = None, category : str = None):
    result_data = {
        "name": author,
    }
    if year is not None:
        result_data["year"] = year
    if category is not None:
        result_data["category"] = category
    return {"data" : result_data}

@app.get("/books/{id}")
def show_book(id : int):
    return {"data" : {"id" : id}}


class Blog(BaseModel):
    title : str
    content : str
    published : Optional[bool] = None

@app.post("/blogs")
def create_blog(blog : Blog):
    return {"data" : f"Blog created with title: {blog.title}, content: {blog.content}, published: {blog.published}"}


class Dictionary(BaseModel):
   name : str
   age : int
   course : str

@app.post("/dictionary")
def create_dictionary(dictionary : Dictionary) :
    return { "data" : dictionary, "message" : f"Welcome, {dictionary.name}!"}

@app.post("/students", response_model=StudentResponse)
def create_student(student : Student) :
    student_response = StudentResponse(id=1, name=student.name, age=student.age)
    return student_response

@app.post("/register")
def register_user(user : UserRegister) :
    if not any(char.isupper() for char in user.password):
        raise HTTPException(status_code=400, detail="Password must contain at least one uppercase letter")
    if not any(char.islower() for char in user.password):
        raise HTTPException(status_code=400, detail="Password must contain at least one lowercase letter")
    if not any(char.isdigit() for char in user.password):
        raise HTTPException(status_code=400, detail="Password must contain at least one digit")
    
    return {"data" : user, "message" : "User registered successfully"}