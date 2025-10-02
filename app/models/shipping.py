from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import mapped_column, Mapped
from app.core.database import Base
from typing import Optional
from pydantic import EmailStr
from datetime import datetime, timezone

class Shipping(Base):
    __tablename__='shipping'

    shipping_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    tracking_code: Mapped[str] = mapped_column(String(100))
    shipping_cost: Mapped[Optional[float]] = mapped_column(Float)
    crated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    delivered_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())

    # Relationships

class ShippingStatus(Base):
    __tablename__='shipping_status'

    status_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    status_name: Mapped[str] = mapped_column(String(20))

    # Relationships

class Sucursal(Base):
    __tablename__='sucursal'

    sucursal_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    IATA: Mapped[str] = mapped_column(String)
    nombre: Mapped[str] = mapped_column(String(100))
    direccion: Mapped[str] = mapped_column(String(100))
    direccion_nro: Mapped[int] = mapped_column(Integer)
    cod_postal: Mapped[int] = mapped_column(Integer)
    tipo: Mapped[Optional[str]] = mapped_column(String(20))
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, default=True)
    
    # Relationships

class Comuna(Base):
    __tablename__='comuna'

    comuna_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))

    # Relationships

class Region(Base):
    __tablename__='region'

    region_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))