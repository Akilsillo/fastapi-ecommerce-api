from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.order import Order, OrderDetail, OrderStatus
from app.schemas.order import *

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, order_data: OrderCreate):
        db_order = Order(**order_data.model_dump())
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order
    
    def get_order(self, order_id: int):
        return self.db.scalar(select(Order).where(Order.order_id == order_id))
    
    def get_all_orders(self):
        return self.db.scalars(select(Order)).all()
    
    def update_order(self, update_date: OrderUpdate, order_id: int):
        db_order = self.get_order(order_id=order_id)
        if db_order:
            for key, value in update_date.model_dump(exclude_unset=True).items():
                setattr(db_order, key, value)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order
    
class OrderDetailRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order_detail(self, detail_data: OrderDetailCreate):
        db_order_detail = OrderDetail(**detail_data.model_dump())
        self.db.add(db_order_detail)
        self.db.commit()
        self.db.refresh(db_order_detail)
        return db_order_detail
    
    def get_order_detail_by_order(self, order_id: int):
        return self.db.scalars(select(OrderDetail).where(OrderDetail.order_id == order_id)).all()
    
    def get_order_detail_by_product(self, product_id: int):
        return self.db.scalars(select(OrderDetail).where(OrderDetail.product_id == product_id)).all()
    
class OrderStatusRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order_status(self, order_status: OrderStatusCreate):
        db_order_status = OrderStatus(**order_status.model_dump())
        self.db.add(db_order_status)
        self.db.commit()
        self.db.refresh(order_status)
        return db_order_status
    
    def get_order_status(self, status_id: int):
        return self.db.scalar(select(OrderStatus).where(OrderStatus.status_id == status_id))