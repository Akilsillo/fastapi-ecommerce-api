from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import mapped_column, Mapped
from app.core.database import Base
from typing import Optional
from pydantic import EmailStr
from datetime import datetime

class Product(Base):
    __tablename__='product'

    product_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(300))
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer)
    image_url: Mapped[Optional[str]] = mapped_column(String)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, default=True)

    # Relationships (tech debt)


class Category(Base):
    __tablename__='category'

    cart_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))

    # Relationships