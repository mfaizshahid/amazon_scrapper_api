
from fastapi import Response, Body
from sqlalchemy.orm import Session
from app.schemas.auth import SignupUserSchema, SigninUserSchema
from app.schemas import response, user
from app.services import users_db
from app.utils.pasword import verify_password
from app.utils.jwt import encode_jwt


class AuthController:
    def signup(self, db: Session, request_payload: SignupUserSchema = Body(...)):
        user_exist = users_db.get_user_by_email(db, request_payload.email)
        if (user_exist):
            return response.GlobalResponse[None](500, "User already exist", None).send()
        user = users_db.create_user(db, request_payload)
        return response.GlobalResponse[None](200, f"{user.name} account created successfully. Please wait while your account get approval from admin", None).send()

    def signin(self, db: Session, request_payload: SigninUserSchema = Body(...)):
        user_exist = users_db.get_user_by_email(db, request_payload.email)
        # If user not exist
        if (not user_exist):
            return response.GlobalResponse[None](500, "Invalid Email/Password", None).send()
        # If account isn't approved yet
        if (not user_exist.is_active):
            return response.GlobalResponse[None](500, "Your Account isn't approved yet", None).send()
        # If wrong password
        if (not verify_password(request_payload.password, user_exist.password)):
            return response.GlobalResponse[None](500, "Invalid Email/Password", None).send()

        # Create JWT
        jwt_token = encode_jwt(str(user_exist.id))
        # User response to send back to client
        user_response = user.SigninUserResponse(
            name=user_exist.name, email=user_exist.email, token=jwt_token)
        return response.GlobalResponse[user.UserBase](200, "User logged in successfully", user_response).send()
