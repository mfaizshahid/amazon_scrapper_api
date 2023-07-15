from fastapi import APIRouter, Response, Body, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import SignupUserSchema, SigninUserSchema
from app.controller.auth import AuthController
from app.dependency.db import get_db_session
auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

auth_controller = AuthController()


@auth_router.post("/signup")
def signup(request_payload: SignupUserSchema = Body(...), db: Session = Depends(get_db_session)):
    return auth_controller.signup(db=db,  request_payload=request_payload)


@auth_router.post("/signin")
def signin(response: Response, request_payload: SigninUserSchema = Body(...), db: Session = Depends(get_db_session)):
    return auth_controller.signin(response=response, request_payload=request_payload)
