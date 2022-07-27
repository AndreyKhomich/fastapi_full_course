from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from .. import models, schemas
from ..hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    if db.query(models.User).filter(request.name == models.User.name) or \
            db.query(models.User).filter(request.email == models.User.email):
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


def get_single(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} is not exist")
    return user


def create_book_for_user(request: schemas.BookCreate, db: Session, user_id: int, ):
    new_book = models.Book(**request.dict(), owner_id=user_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
