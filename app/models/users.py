from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from app.core.database import Base
from typing import Optional
from pydantic import EmailStr
from datetime import datetime

class User(Base):
    __tablename__='user'

    id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    surname: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean)
    role: Mapped[Optional[str]] = mapped_column(String(20), default='customer')
    created_at: Mapped[datetime] = mapped_column(DateTime)