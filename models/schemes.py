from pydantic import BaseModel, EmailStr, Field
from typing import List,Optional,Type
from datetime import timedelta

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)
    email: str = Field(...,min_length=8, max_length=60)


class Movie(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    genre: str = Field(..., min_length=3, max_length=50)
    rating: float= Field(..., ge=0, le=10)    


class Rental(BaseModel):
    user: User  
    movie: Movie  
    rental_duration: int = Field(..., ge=1)  


class TokenData(BaseModel):
    username: str

class LoginRequest(BaseModel):
    username: str = Field(...)
    password: str = Field(...)