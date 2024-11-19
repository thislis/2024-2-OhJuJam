from sqlalchemy import Column, Integer, String
from database.database import Base


class Door(Base):
    __tablename__ = "Door"

    id = Column(Integer, primary_key=True, index=True)
    room_num = Column(Integer, unique=True, nullable=True)
    opened = Column(Integer, unique=True)