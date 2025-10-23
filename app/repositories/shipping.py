from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.shipping import Shipping, ShippingStatus, Sucursal, Comuna, Region
from app.schemas.shipping import *

class ShippingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_shipping(self, shipping_data: ShippingCreate):
        db_shipping = Shipping(**shipping_data.model_dump())
        self.db.add(db_shipping)
        self.db.commit()
        self.db.refresh(db_shipping)
        return db_shipping
    
    def get_shipping(self, shipping_id: int):
        return self.db.scalar(select(Shipping).where(Shipping.shipping_id == shipping_id))
    
    def get_all_shippings(self):
        return self.db.scalars(select(Shipping)).all()
    
    def update_shipping(self, update_data: ShippingUpdate, shipping_id: int):
        db_shipping = self.get_shipping(shipping_id=shipping_id)
        if db_shipping:
            for key, value in update_data.model_dump(exclude_unset=True).items():
                setattr(db_shipping, key, value)
        self.db.commit()
        self.db.refresh(db_shipping)
        return db_shipping
    
class ShippingStatusRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_shipping_status(self, shipping_status: ShippingStatusCreate):
        db_shipping_status = ShippingStatus(**shipping_status.model_dump())
        self.db.add(db_shipping_status)
        self.db.commit()
        self.db.refresh(db_shipping_status)
        return db_shipping_status
    
    def get_shipping_status(self, status_id: int):
        return self.db.scalar(select(ShippingStatus).where(ShippingStatus.status_id == status_id))
    
class SucursalRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_sucursal(self, sucursal_data: SucursalCreate):
        db_sucursal = Sucursal(**sucursal_data.model_dump())
        self.db.add(db_sucursal)
        self.db.commit()
        self.db.refresh(db_sucursal)
        return db_sucursal
    
    def get_sucursal(self, sucursal_id: int):
        return self.db.scalar(select(Sucursal).where(Sucursal.sucursal_id == sucursal_id))
    
    def get_all_sucursals(self):
        return self.db.scalars(select(Sucursal)).all()
    
    def update_sucursal(self, update_data: SucursalCreate, sucursal_id: int):
        db_sucursal = self.get_sucursal(sucursal_id=sucursal_id)
        if db_sucursal:
            for key, value in update_data.model_dump(exclude_unset=True).items():
                setattr(db_sucursal, key, value)
        self.db.commit()
        self.db.refresh(db_sucursal)
        return db_sucursal

class ComunaRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_comuna(self, comuna_data: ComunaCreate):
        db_comuna = Comuna(**comuna_data.model_dump())
        self.db.add(db_comuna)
        self.db.commit()
        self.db.refresh(db_comuna)
        return db_comuna

    def get_comuna(self, comuna_id: int):
        return self.db.scalar(select(Comuna).where(Comuna.comuna_id == comuna_id))
    
    def get_all_comunas(self):
        return self.db.scalars(select(Comuna)).all()
    
class RegionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_region(self, region_data: RegionCreate):
        db_region = Region(**region_data.model_dump())
        self.db.add(db_region)
        self.db.commit()
        self.db.refresh(db_region)
        return db_region

    def get_region(self, region_id: int):
        return self.db.scalar(select(Region).where(Region.region_id == region_id))
    
    def get_all_regions(self):
        return self.db.scalars(select(Region)).all()