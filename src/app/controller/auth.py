
from fastapi import Response, Body
from app.schemas.auth import SignupUserSchema, SigninUserSchema


class AuthController:
    async def signup(self, response: Response, request_payload: SignupUserSchema = Body(...)):
        print("Signup", request_payload)
        return "singup"

    async def signin(self, response: Response, request_payload: SigninUserSchema = Body(...)):
        print("Signin", request_payload)
        return "signin"
