from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status
from database.database import get_db

from database.models import Door


router = APIRouter(
    prefix="/opendoor",
    tags=["door_game"]
)

@router.get("/main/load")
def load_main_door(db: Session = Depends(get_db)):
    main_door_state = db.query(Door).filter(Door.room_num == 0).first()
    main_door_state = main_door_state.__asdict()
    return {"main_door_state": main_door_state["opened"]}

@router.post("/main/open")
def update_main_door(form_data, db: Session = Depends(get_db)):
