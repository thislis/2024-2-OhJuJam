from sqlalchemy.orm import Session
from src.schema.user_schema import UserCreate
from database.models import User

def create_user(db: Session, user_create: UserCreate):
    db_user = User(name=user_create.username)
    db.add(db_user)
    db.commit()


def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.name == user_create.username)
    ).first()


def get_user(db: Session, username: str):
    return db.query(User).filter(User.name == username).first()