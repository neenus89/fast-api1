from fastapi import FastAPI

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

