from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from schemas import Student

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

@app.post("/students")
def create_student(student : Student):
    return {"data" : student, "message" : f"Student {student.name} created successfully!"}