from fastapi import APIRouter, Response, Body
from app.models.auth import SignupUserSchema, SigninUserSchema
from app.controller.auth import AuthController
auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

auth_controller = AuthController()


@auth_router.post("/signup")
async def signup(response: Response, request_payload: SignupUserSchema = Body(...),):
    return await auth_controller.signup(response=response, request_payload=request_payload)


@auth_router.post("/signin")
async def signin(response: Response, request_payload: SigninUserSchema = Body(...),):
    return await auth_controller.signin(response=response, request_payload=request_payload)
