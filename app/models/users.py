from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.core.database import Base
from typing import Optional, List
from pydantic import EmailStr
from datetime import datetime

from app.models.order import *
from app.models.cart import *

class User(Base):
    __tablename__='user'

    user_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    surname: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean)
    role: Mapped[Optional[str]] = mapped_column(String(20), default='customer')
    created_at: Mapped[datetime] = mapped_column(DateTime)

    # Relationships
    orders: Mapped[List['Order']] = relationship(back_populates='user')
    carts: Mapped[List['Cart']] = relationship(back_populates='user')