
from fastapi import Body
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.auth import SignupUserSchema, SigninUserSchema
from app.schemas import response, user
from app.services import users_db, roles_db
from app.models import roles as RolesModel
from app.types.roles import RoleTypes
from app.utils.pasword import verify_password
from app.utils.jwt import encode_jwt
from dotenv import load_dotenv
import os
load_dotenv()


class AuthController:
    def signup(self, db: Session, request_payload: SignupUserSchema = Body(...)):
        user_exist = users_db.get_user_by_email(db, request_payload.email)
        if (user_exist):
            return response.GlobalResponse[None](500, "User already exist", None).send()
        user = users_db.create_user(db, request_payload)
        if (not user):
            return response.GlobalResponse[None](500, "Failed to create account", None).send()
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

        user_role = roles_db.get_role_by_id(
            db, user_exist.role_id)
        jwt_secret = os.environ.get(
            "jwt_secret") if user_role.name == RoleTypes.USER else os.environ.get("admin_jwt_secret")
        # Create JWT
        jwt_token = encode_jwt(str(user_exist.id), jwt_secret)
        # User response to send back to client
        user_response = user.SigninUserResponse(
            name=user_exist.name, email=user_exist.email, token=jwt_token)
        return response.GlobalResponse[user.UserBase](200, "User logged in successfully", user_response).send()
