from fastapi import Response
from typing import TypeVar, Generic

T = TypeVar('T')


class GlobalResponse(Generic[T]):
    def __init__(self, status_code: int, message: str, data: T):
        self.status_code = status_code
        self.message = message
        self.data = data

    def send(self):
        return {
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data
        }
