from app.models.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Boolean, Integer, Column, UUID, DateTime, func, Text
import uuid


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = Column(UUID(as_uuid=True), primary_key=True,
                                   index=True, default=uuid.uuid4)
    name: Mapped[str] = Column(String(255), nullable=False)
    email: Mapped[str] = Column(String(255), unique=True, nullable=False)
    password: Mapped[str] = Column(String(255), nullable=False)
    is_active: Mapped[bool] = Column(Boolean, default=False, nullable=False)
    created_at: Mapped[str] = Column(
        DateTime(timezone=False), server_default=func.now(), nullable=False)
    updated_at: Mapped[str] = Column(
        DateTime(timezone=False), onupdate=func.now())
