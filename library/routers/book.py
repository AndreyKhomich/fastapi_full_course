from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from library import database, schemas, oath2
from ..data_base import book


router = APIRouter(
    prefix="/book",
    tags=['Books']
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBook])
def get_books(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Book,  db: Session = Depends(get_db),  get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.create(request, db)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.delete(book_id, db)


@router.put("/{book_id}", status_code=status.HTTP_202_ACCEPTED)
def update_book(book_id: int, request: schemas.Book, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.update(book_id, request, db)


@router.get("/{book_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBook)
def get_single_book(book_id: int, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return book.get_single(book_id, db)
