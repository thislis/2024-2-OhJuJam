from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status
from database.database import get_db

from database.models import Door
import src.CRUD.door_crud as door_crud


router = APIRouter(
    prefix="/opendoor",
    tags=["door_game"]
)

@router.get("/load/{door_num}")
def load_door(db: Session = Depends(get_db)):
    door_num = door_num
    main_door_state = db.query(Door).filter(Door.room_num == door_num).first()
    main_door_state = main_door_state.__asdict()
    return {"main_door_state": main_door_state["opened"]}

@router.post("/open")
def update_door(form_data, db: Session = Depends(get_db)):
    door = door_crud.get_door(db, form_data.doornum)
    if not door:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect or Not exist number of the door",
            headers={"WWW-Authenticate": "Bearer"},
        )
    door_crud.update_door(db, form_data.doornum, form_data.dooropen)

    return {"message": "Success"}

@router.post("/create")
def create_door(door_create_: door_crud.DoorCreate, db: Session = Depends(get_db)):
    door_crud.create_door(db, door_create=door_create_)
    
    return {"message": "Success"}