from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from database.database import get_db
import src.CRUD.user_crud as user_crud
import src.schema.user_schema as user_schema

router = APIRouter(
    prefix="/account",
    tags=["sign_up"]
)


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user_crud.create_user(db=db, user_create=_user_create)

    return {"message": "Success"}