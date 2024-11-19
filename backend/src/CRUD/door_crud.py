import random

from sqlalchemy.orm import Session
from src.schema.door_schema import DoorCreate
from database.models import Door


def get_door(db: Session, door_num: int):
    return db.query(Door).filter(Door.room_num == door_num).first()


def create_door(db: Session, door_create: DoorCreate):
    
    door_num = door_create.door_num
    
    while not door_num:
        num = random.randrange(1, 100000)
        if get_door(db, num):
            continue
        else:
            door_num = num

    db_door = Door(room_num=door_num, opened=0)
    db.add(db_door)
    db.commit()


def get_existing_door(db: Session, door_create: DoorCreate):
    return db.query(Door).filter(
        (Door.room_num == door_create.door_num)
    ).first()


def update_door(db: Session, door_num: int, door_open: int):
    value = door_open * db.query(Door).filter_by(door_num=door_num).opened
    db.query(Door).filter_by(door_num=door_num).update({"opened": value})
    db.commit()
    