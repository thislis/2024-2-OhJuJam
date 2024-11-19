from sqlalchemy.orm import Session
from src.schema.door_schema import DoorCreate
from database.models import Door

def create_door(db: Session, door_create: DoorCreate):
    db_door = Door(room_num=door_create.door_num, opened=0)
    db.add(db_door)
    db.commit()


def get_existing_door(db: Session, door_create: DoorCreate):
    return db.query(Door).filter(
        (Door.room_num == door_create.door_num)
    ).first()


def get_door(db: Session, door_num: int):
    return db.query(Door).filter(Door.room_num == door_num).first()


def update_door(db: Session, door_num: int, door_open: int):
    value = door_open * db.query(Door).filter_by(door_num=door_num).opened
    db.query(Door).filter_by(door_num=door_num).update({"opened": value})
    db.commit()
    