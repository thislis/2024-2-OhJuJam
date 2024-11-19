from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

import src.CRUD.user_crud as user_crud
from database.database import get_db

router = APIRouter(
    prefix="/account",
    tags=["sign_in"]
)

@router.post("/login")
def login(form_data, db: Session = Depends(get_db)):

    user = user_crud.get_user(db, form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect or Not exist username",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "username": user.username
    }