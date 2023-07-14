from pydantic import BaseModel, Field, EmailStr


class SignupUserSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)


class SigninUserSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
