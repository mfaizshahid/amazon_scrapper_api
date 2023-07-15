from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool = False
    created_at: str
    updated_at: str | None = None


class User(UserBase):
    id: str

    class Config:
        orm_mode = True
