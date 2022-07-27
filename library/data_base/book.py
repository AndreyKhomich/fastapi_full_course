from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from library import models, schemas
from sqlalchemy.sql import exists


def get_all(db: Session):
    books = db.query(models.Book).all()
    return books


def delete(book_id: int, db: Session):
    book = db.query(models.Book).filter(models.Book.id == book_id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} does not exist")
    book.delete(synchronize_session=False)
    db.commit()
    return "The  library was deleted"


def update(book_id: int, request: schemas.Book, db: Session):
    book = db.query(models.Book).filter(models.Book.id == book_id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} does not exist")
    book.update(request.dict())
    db.commit()
    return 'Updated'


def get_single(book_id: int, db: Session):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} is not available")
    return book
