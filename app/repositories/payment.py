from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.payment import Payment, PaymentMethod, PaymentStatus
from app.schemas.payment import *

class PaymentMethodRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def create_payment_method(self, payment_method: PaymentMethodCreate):
        db_method = PaymentMethod(**payment_method.model_dump())
        self.db.add(db_method)
        self.db.commit()
        self.db.refresh(db_method)
        return db_method
    
    def get_payment_method(self, method_id: int):
        return self.db.scalar(select(PaymentMethod).where(PaymentMethod.pmethod_id == method_id))
    
    def get_all_payment_method(self) -> List[PaymentMethodOut]:
        return self.db.scalars(select(PaymentMethod)).all()
    
class PaymentStatusRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_payment_status(self, status: PaymentStatusCreate):
        db_status = PaymentStatus(**status.model_dump())
        self.db.add(db_status)
        self.db.commit()
        self.db.refresh(db_status)
        return db_status
    
    def get_payment_status(self, status_id: int):
        return self.db.scalar(select(PaymentStatus).where(PaymentStatus.status_id == status_id))
    
class PaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_payment(self, payment: PaymentCreate):
        db_payment = Payment(**payment.model_dump())
        self.db.add(db_payment)
        self.db.commit()
        self.db.refresh(db_payment)
        return db_payment
    
    def get_payment(self, payment_id: int):
        return self.db.scalar(select(Payment).where(Payment.payment_id == payment_id))
    
    def get_all_payments(self):
        return self.db.scalars(select(Payment)).all()
    
    def update_payment(self, payment_update: PaymentUpdate, payment_id: int):
        db_payment = self.get_payment(payment_id=payment_id)
        if db_payment:
            for key, value in payment_update.model_dump(exclude_unset=True).items():
                setattr(db_payment, key, value)
            self.db.commit()
            self.db.refresh(db_payment)
        return db_payment