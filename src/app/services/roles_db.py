from sqlalchemy.orm import Session
from app.models import roles as RolesModel
import uuid


def get_role_by_name(db: Session, role: str) -> RolesModel.Role | None:
    return db.query(RolesModel.Role).filter(RolesModel.Role.name == role).first()


def get_role_by_id(db: Session, role: uuid.UUID) -> RolesModel.Role | None:
    return db.query(RolesModel.Role).get(role)
