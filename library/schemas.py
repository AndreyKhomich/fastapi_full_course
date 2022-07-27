from typing import List, Optional
from pydantic import BaseModel, Field


class BaseBook(BaseModel):
    title: str
    author: str

    class Config:
        orm_mode = True


class BookCreate(BaseBook):
    pass


class Book(BaseBook):
    id: int
    owner_id: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    books: List["Book"]

    class Config:
        orm_mode = True


class ShowBook(BaseModel):
    title: str
    author: str
    reader: ShowUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
