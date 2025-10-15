from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.core.database import Base
from typing import Optional, List
from pydantic import EmailStr
from datetime import datetime

from app.models.product import *
from app.models.users import *

class Cart(Base):
    __tablename__='cart'

    cart_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2))

    # Foreign Keys
    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    status_id: Mapped[int] = mapped_column(ForeignKey('cart_status.status_id'))

    # Relationships
    user: Mapped['User'] = relationship(back_populates='carts')
    status: Mapped['CartStatus'] = relationship(back_populates='carts')
    cart_items: Mapped[List['CartItem']] = relationship(back_populates='cart')

class CartItem(Base):
    __tablename__='cart_item'

    quantity: Mapped[int] = mapped_column(Integer)
    subtotal: Mapped[float] = mapped_column(Numeric(10, 2))

    # Foreign Keys
    cart_id: Mapped[int] = mapped_column(ForeignKey('cart.cart_id'), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.product_id'), primary_key=True)

    # Relationships
    cart: Mapped['Cart'] = relationship(back_populates='cart_items')
    product: Mapped['Product'] = relationship(back_populates='cart_item')

class CartStatus(Base):
    __tablename__='cart_status'

    status_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    status_name: Mapped[str] = mapped_column(String(25))

    # Relationships
    carts: Mapped[List['Cart']] = relationship(back_populates='status')