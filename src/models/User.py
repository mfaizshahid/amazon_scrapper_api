from pydantic import BaseModel


class User(BaseModel):
    name: str
    username: str
    password: str
    active: str
