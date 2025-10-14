from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import datetime

from app.schemas.order import OrderOut, OrderCreate

# Shipping Schemas

class ShippingCreate(BaseModel):
    order_id: int
    sucursal_id: int
    status_id: int
    tracking_code: str = Field(max_length=100)
    shipping_cost: Optional[float] = None

class ShippingOut(BaseModel):
    shipping_id: int
    order_id: int
    sucursal_id: int
    status_id: int
    tracking_code: str
    shipping_cost: Optional[float] = None
    crated_at: str
    delivered_at: Optional[str] = None
    is_active: Optional[bool] = True

    order: Optional[OrderOut]

    model_config = ConfigDict(from_attributes=True)

class ShippingUpdate(BaseModel):

    sucursal_id: Optional[int] = None
    status_id: Optional[int] = None
    shipping_cost: Optional[float] = None
    delivered_at: Optional[datetime] = None
    is_active: Optional[bool] = None

# Shipping Status Schemas

class ShippingStatusCreate(BaseModel):
    status_name: str = Field(max_length=20)

class ShippingStatusOut(BaseModel):
    status_id: int
    status_name: str

    model_config = ConfigDict(from_attributes=True)

# Sucursal Schemas

class SucursalCreate(BaseModel):
    IATA: str
    nombre: str = Field(max_length=100)
    direccion: str = Field(max_length=100)
    direccion_nro: int
    cod_postal: int
    tipo: Optional[str] = Field(default=None, max_length=20)
    is_active: Optional[bool] = True
    comuna_id: int

class SucursalOut(BaseModel):
    sucursal_id: int
    IATA: str
    nombre: str
    direccion: str
    direccion_nro: int
    cod_postal: int
    tipo: Optional[str] = None
    is_active: Optional[bool] = True
    comuna_id: int

    model_config = ConfigDict(from_attributes=True)

class SucursalUpdate(BaseModel):

    IATA: Optional[str] = None
    nombre: Optional[str] = Field(default=None, max_length=100)
    direccion: Optional[str] = Field(default=None, max_length=100)
    direccion_nro: Optional[int] = None
    cod_postal: Optional[int] = None
    tipo: Optional[str] = Field(default=None, max_length=20)
    is_active: Optional[bool] = None
    comuna_id: Optional[int] = None

# Comuna Schemas

class ComunaCreate(BaseModel):
    name: str = Field(max_length=30)
    region_id: int

class ComunaOut(BaseModel):
    comuna_id: int
    name: str
    region_id: int

    model_config = ConfigDict(from_attributes=True)

# Region Schemas

class RegionCreate(BaseModel):
    name: str = Field(max_length=50)

class RegionOut(BaseModel):
    region_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)