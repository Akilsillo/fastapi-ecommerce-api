from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.core.database import Base
from typing import Optional, List
from pydantic import EmailStr
from datetime import datetime

from app.models.cart import *
from app.models.order import *

class Product(Base):
    __tablename__='product'

    product_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(300))
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer)
    image_url: Mapped[Optional[str]] = mapped_column(String)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, default=True)

    # Foreign Keys
    cat_id: Mapped[int] = mapped_column(ForeignKey('category.cat_id'))

    # Relationships (tech debt)
    cart_item: Mapped[List['CartItem']] = relationship(back_populates='product')
    category: Mapped['Category'] = relationship(back_populates='products')
    order_detail: Mapped[List['OrderDetail']] = relationship(back_populates='product')

class Category(Base):
    __tablename__='category'

    cat_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))

    # Relationships
    products: Mapped[List['Product']] = relationship(back_populates='category')