
from fastapi import Body, Depends
from sqlalchemy.orm import Session
from app.schemas.admin import ActiveUserSchema
from app.schemas.auth import SigninUserSchema
from app.schemas import response, user
from app.services import users_db, roles_db
from app.middlewares.token import verify_admin_token


class AdminController:
    def user_account_action(self, db: Session, request_payload: ActiveUserSchema = Body(...), user_id: str = Depends(verify_admin_token)):
        user_exist = users_db.get_user_by_email(db, request_payload.email)
        if (not user_exist):
            return response.GlobalResponse[None](500, "User not exist", None).send()
        user = users_db.user_account_action(db, request_payload, user_exist)
        return response.GlobalResponse[None](200, f"Account Action Status: {user.is_active}", None).send()
