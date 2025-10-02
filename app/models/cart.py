from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import mapped_column, Mapped
from app.core.database import Base
from typing import Optional
from pydantic import EmailStr
from datetime import datetime

class Cart(Base):
    __tablename__='cart'

    cart_id = Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    created_at = Mapped[datetime] = mapped_column(DateTime)
    total_amount = Mapped[float] = mapped_column(Float)

    # Relationships

class CartItem(Base):
    __tablename__='cart_item'

    quantity = Mapped[int] = mapped_column(Integer)
    subtotal = Mapped[float] = mapped_column(Float)

    # Relationships

class CartStatus(Base):
    __tablename__='cart_state'

    state_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    state_name: Mapped[str] = mapped_column(String(25))

    # Relationships