from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str


class User(UserBase):
    id: str
    password: str
    is_active: bool = False
    created_at: str
    updated_at: str | None = None

    class Config:
        orm_mode = True


class SigninUserResponse(UserBase):
    token: str
