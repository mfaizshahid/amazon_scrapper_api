from sqlalchemy.orm import Session
from app.schemas.auth import SignupUserSchema
from app.utils.pasword import get_password_hash
from app.models import user as UserModel


def create_user(db: Session, user: SignupUserSchema) -> UserModel.User:
    hashed_password = get_password_hash(user.password)
    db_user = UserModel.User(email=user.email, password=hashed_password,
                             name=user.name, is_active=False)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str) -> UserModel.User | None:
    return db.query(UserModel.User).filter(UserModel.User.email == email).first()
