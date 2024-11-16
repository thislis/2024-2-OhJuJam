from sqlalchemy import Column, Integer, String
from database import Base

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
    
