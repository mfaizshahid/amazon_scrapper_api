from fastapi import APIRouter,  Body, Depends
from sqlalchemy.orm import Session
from app.schemas.admin import ActiveUserSchema
from app.controller.admin import AdminController
from app.dependency.db import get_db_session
from app.middlewares.token import get_token_from_header, verify_admin_token

admin_router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(get_token_from_header), Depends(verify_admin_token)]
)

admin_controller = AdminController()


@admin_router.patch("/user-action")
def user_account_action(request_payload: ActiveUserSchema = Body(...), db: Session = Depends(get_db_session)):
    return admin_controller.user_account_action(db=db,  request_payload=request_payload)
