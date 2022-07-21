from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas


def get_all(db: Session):
    books = db.query(models.Book).all()
    return books


def create(request: schemas.Book, db: Session):
    new_book = models.Book(title=request.title, author=request.author, user_id=1)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def destroy(id: int, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} does not exist")
    book.delete(synchronize_session=False)
    db.commit()
    return "The  library was deleted"


def update(id: int, request: schemas.Book, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} does not exist")
    book.update(request.dict())
    db.commit()
    return 'Updated'


def get_single(id: int, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} is not available")
    return book
