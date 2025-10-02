from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import mapped_column, Mapped
from app.core.database import Base
from typing import Optional
from pydantic import EmailStr
from datetime import datetime

class Order(Base):
    __tablename__='order'

    order_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    total_amount: Mapped[float] = mapped_column(Float)

    # Relationships

class OrderDetail(Base):
    __tablename__='order_detail'

    quantity: Mapped[int] = mapped_column(Integer)
    subtotal: Mapped[float] = mapped_column(Float)
    product_price: Mapped[float] = mapped_column(Float)

    # Relationships

class OrderStatus(Base):
    __tablename__='order_status'

    status_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    status_name: Mapped[str] = mapped_column(String(25))

    # Relationships