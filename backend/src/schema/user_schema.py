from pydantic import BaseModel, validator

class UserCreate(BaseModel):
    username: str

    @validator('username')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v