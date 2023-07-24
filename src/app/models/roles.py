from app.models.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy import String, Boolean, Integer, Column, UUID, DateTime, func, Text
import uuid


class Role(Base):
    __tablename__ = "roles"
    id: Mapped[uuid.UUID] = Column(UUID(as_uuid=True), primary_key=True,
                                   default=uuid.uuid4)
    name: Mapped[str] = Column(String(255), nullable=False)
    is_active: Mapped[bool] = Column(Boolean, default=True, nullable=False)
    created_at: Mapped[str] = Column(
        DateTime(timezone=False), server_default=func.now(), nullable=False)
    updated_at: Mapped[str] = Column(
        DateTime(timezone=False), onupdate=func.now())
