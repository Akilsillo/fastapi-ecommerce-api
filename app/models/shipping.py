from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.core.database import Base
from typing import Optional, List
from pydantic import EmailStr
from datetime import datetime, timezone

from app.models.order import *

class Shipping(Base):
    __tablename__='shipping'

    shipping_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    tracking_code: Mapped[str] = mapped_column(String(100))
    shipping_cost: Mapped[Optional[float]] = mapped_column(Float)
    crated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    delivered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    # Foreign Keys
    order_id: Mapped[int] = mapped_column(ForeignKey('order.order_id'))
    sucursal_id: Mapped[int] = mapped_column(ForeignKey('sucursal.sucursal_id'))
    status_id: Mapped[int] = mapped_column(ForeignKey('shipping_status.status_id'))

    # Relationships
    order: Mapped['Order'] = relationship(back_populates='shipping')
    sucursal: Mapped['Sucursal'] = relationship(back_populates='shippings')
    status: Mapped['ShippingStatus'] = relationship(back_populates='shippings')

class ShippingStatus(Base):
    __tablename__='shipping_status'

    status_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    status_name: Mapped[str] = mapped_column(String(20))

    # Relationships
    shippings: Mapped['Shipping'] = relationship(back_populates='status')

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

    # Foreign Keys
    comuna_id: Mapped[int] = mapped_column(ForeignKey('comuna.comuna_id'))
    
    # Relationships
    shippings: Mapped[List['Shipping']] = relationship(back_populates='sucursal')
    comuna: Mapped['Comuna'] = relationship(back_populates='sucursales')

class Comuna(Base):
    __tablename__='comuna'

    comuna_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))

    # Foreign Keys
    region_id: Mapped[int] = mapped_column(ForeignKey('region.region_id'))

    # Relationships
    sucursales: Mapped[List['Sucursal']] = relationship(back_populates='comuna')
    region: Mapped['Region'] = relationship(back_populates='comunas')

class Region(Base):
    __tablename__='region'

    region_id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))

    # Relationships

    comunas: Mapped[List['Comuna']] = relationship(back_populates='region')