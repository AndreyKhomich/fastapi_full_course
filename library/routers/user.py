from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..data_base import user
from library import schemas, database, oath2

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db


@router.post("/", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{user_id}", response_model=schemas.ShowUser)
def get_user(user_id, db: Session = Depends(get_db)):
    return user.get_single(user_id, db)


@router.post("/{user_id}/book", status_code=status.HTTP_201_CREATED, response_model=schemas.Book)
def create_book(user_id: int, request: schemas.BookCreate, db: Session = Depends(get_db),
                get_current_user: schemas.User = Depends(oath2.get_current_user)):
    return user.create_book_for_user(request, db, user_id=user_id)
