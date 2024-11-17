from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from database.database import get_db
from CRUD import user_crud
from schema import user_schema

router = APIRouter(
    prefix="/account",
)


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user_crud.create_user(db=db, user_create=_user_create)