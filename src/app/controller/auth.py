
from fastapi import Response, Body
from sqlalchemy.orm import Session
from app.schemas.auth import SignupUserSchema, SigninUserSchema
from app.schemas import response
from app.services import users_db


class AuthController:
    def signup(self, db: Session, request_payload: SignupUserSchema = Body(...)):
        user_exist = users_db.get_user_by_email(db, request_payload.email)
        if (user_exist):
            return response.GlobalResponse[None](500, "User already exist", None).send()
        user = users_db.create_user(db, request_payload)
        return response.GlobalResponse[None](200, f"{user.name} account created successfully. Please wait while your account get approval from admin", None).send()

    def signin(self, response: Response, request_payload: SigninUserSchema = Body(...)):
        print("Signin", request_payload)
        return "signin"
