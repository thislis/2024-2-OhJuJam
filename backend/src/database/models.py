from sqlalchemy import Column, Integer, String, Table, MetaData
from database import Base


class Door(Base):
    __tablename__ = "Door"

    id = Column(Integer, primary_key=True, index=True)
    room_num = Column(Integer, unique=True, nullable=True)
    opened = Column(Integer, unique=True)


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    pw = Column(String)


class Game_result(Base):
    __tablename__ = "Game_result"

    user_name = Column(String, unique=True, nullable=False)
    game_name = Column(String, unique=True, nullable=False)
    how_many_play= Column(Integer, nullable=False)
    how_many_win = Column(Integer, nullable=False)