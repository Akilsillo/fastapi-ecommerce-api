from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.core.database import Base
from typing import Optional
from pydantic import EmailStr
from datetime import datetime

from app.models.product import *
from app.models.users import *
from app.models.payment import *
from app.models.shipping import *

class Order(Base):
    __tablename__='order'

    order_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2))
    
    # Foreign Keys
    status_id: Mapped[int] = mapped_column(ForeignKey('order_status.status_id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))

    # Relationships
    order_detail: Mapped[List['OrderDetail']] = relationship(back_populates='order')
    status: Mapped['OrderStatus'] = relationship(back_populates='orders')
    user: Mapped['User'] = relationship(back_populates='orders')
    payment: Mapped['Payment'] = relationship(back_populates='order')
    shipping: Mapped['Shipping'] = relationship(back_populates='order')

class OrderDetail(Base):
    __tablename__='order_detail'

    quantity: Mapped[int] = mapped_column(Integer)
    subtotal: Mapped[float] = mapped_column(Numeric(10, 2))
    product_price: Mapped[float] = mapped_column(Numeric(10, 2))

    # Foreign Keys
    order_id: Mapped[int] = mapped_column(ForeignKey('order.order_id'), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.product_id'), primary_key=True)

    # Relationships
    product: Mapped['Product'] = relationship(back_populates='order_detail')
    order: Mapped['Order'] = relationship(back_populates='order_detail')

class OrderStatus(Base):
    __tablename__='order_status'

    status_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    status_name: Mapped[str] = mapped_column(String(25))

    # Relationships
    orders: Mapped[List['Order']] = relationship(back_populates='status')