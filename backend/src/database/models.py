from sqlalchemy import Column, Integer, String, Table, MetaData
from database import Base

user_game_result = Table(
    'user_game_result',
    metadata=MetaData(),
    id = Column(Integer, primary_key=True, index=True),
    game_name = Column(String, nullable=False),
    how_many_play = Column(Integer, nullable=False),
    how_many_win = Column(Integer, nullable=False)
)

class Door(Base):
    __tablename__= "Door"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer, unique=True)
    opened = Column(Integer, unique=True)


class User(Base):
    __tablename__= "User"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    pw = Column(String)

