
from fastapi import FastAPI

from . import models
from .database import engine
from .routers import book, user, authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(book.router)
app.include_router(user.router)


models.Base.metadata.create_all(bind=engine)

