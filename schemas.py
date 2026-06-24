from pydantic import BaseModel, Field, EmailStr


class Student(BaseModel) :
    name : str
    age : int

class StudentResponse(BaseModel) :
    id : int
    name : str
    age : int

class UserRegister(BaseModel) :
    email: EmailStr 
    age: int = Field(..., ge=18, le=60) 
    password: str = Field(..., min_length=8)
