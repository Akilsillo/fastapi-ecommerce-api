from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.core.database import Base
from typing import Optional, List
from pydantic import EmailStr
from datetime import datetime

from app.models.order import *

class Payment(Base):
    __tablename__='payment'

    payment_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    payment_gateway: Mapped[str] = mapped_column(String(30))
    transaction_id: Mapped[int] = mapped_column(Integer)
    amount: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    
    # Foreign Keys
    order_id: Mapped[int] = mapped_column(ForeignKey('order.order_id'))
    pmethod_id: Mapped[int] = mapped_column(ForeignKey('payment_method.pmethod_id'))

    # Relationships
    method: Mapped['PaymentMethod'] = relationship(back_populates='payments')
    order: Mapped['Order'] = relationship(back_populates='payment')

class PaymentMethod(Base):
    __tablename__='payment_method'

    pmethod_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    method_name: Mapped[str] = mapped_column(String(30))

    # Relationships
    payments: Mapped[List['Payment']] = relationship(back_populates='method')