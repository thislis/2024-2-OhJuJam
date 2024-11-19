from pydantic import BaseModel, validator

class DoorCreate(BaseModel):
    door_num: int

    @validator('door_state')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v