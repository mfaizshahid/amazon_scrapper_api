from sqlalchemy.orm import Session
from app.schemas.auth import SignupUserSchema
from app.schemas.admin import ActiveUserSchema
from app.utils.pasword import get_password_hash
from app.models import user as UserModel
from app.types.roles import RoleTypes
from .roles_db import get_role_by_name


def create_user(db: Session, user: SignupUserSchema) -> UserModel.User | None:
    user_role = get_role_by_name(db, RoleTypes.USER)
    if (not user_role):
        return None
    hashed_password = get_password_hash(user.password)
    db_user = UserModel.User(email=user.email, password=hashed_password,
                             name=user.name, is_active=False, role_id=user_role.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str) -> UserModel.User | None:
    return db.query(UserModel.User).filter(UserModel.User.email == email).first()


def user_account_action(db: Session, payload: ActiveUserSchema, user: UserModel.User):
    user.is_active = payload.is_active
    db.commit()
    return user
