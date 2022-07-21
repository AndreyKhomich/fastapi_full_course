from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from library import database, schemas, oath2
from ..repository import book


router = APIRouter(
    prefix="/book",
    tags=['Books']
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBook])
def get_books(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Book, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_book(id: int, request: schemas.Book, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.update(id, request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBook)
def get_single_book(id: int, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.get_single(id, db)
