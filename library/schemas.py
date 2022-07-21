from typing import List, Union, Optional
from pydantic import BaseModel


class BaseBook(BaseModel):
    title: str
    author: str


class Book(BaseBook):

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
    creator: ShowUser

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
