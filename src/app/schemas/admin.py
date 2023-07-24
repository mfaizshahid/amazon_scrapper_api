from pydantic import BaseModel


class ActiveUserSchema(BaseModel):
    email: str
    is_active: bool
