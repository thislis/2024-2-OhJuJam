from pydantic import BaseModel

class DoorCreate(BaseModel):
    door_num: int