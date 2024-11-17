from passlib.context import CryptContext
from sqlalchemy.orm import Session
from backend.src.schema.user_schema import UserCreate
from backend.database.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user_create: UserCreate):
    db_user = User(name=user_create.username,
                   pw=pwd_context.hash(user_create.password1)
                )
    db.add(db_user)
    db.commit()


def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.name == user_create.username)
    ).first()


def get_user(db: Session, username: str):
    return db.query(User).filter(User.name == username).first()