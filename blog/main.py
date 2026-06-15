from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Blog(BaseModel):
    title : str
    content : str

@app.post("/blog")
def create(request : Blog):
    return {"data" : f"Blog created with title: {request.title} and body: {request.content}"}