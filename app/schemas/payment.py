from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List

from app.schemas.product import ProductOut
from app.schemas.users import UserOut
from app.schemas.order import OrderCreate, OrderOut

# Payment Schemas

class PaymentCreate(BaseModel):
    order_id: int
    payment_gateway: str = Field(max_length=25)
    transaction_id: int
    amount: float
    pmethod_id: int
    status_id: int
    currency: str

class PaymentOut(BaseModel):
    payment_id: int
    order_id: int
    payment_gateway: str
    transaction_id: int
    amount: float
    currency: str
    created_at: str
    updated_at: str
    pmethod_id: int
    status_id: int

    order: Optional[OrderOut]

    model_config = ConfigDict(from_attributes=True)

class PaymentUpdate(BaseModel):
    currency: Optional[str] = None
    pmethod_id: Optional[int] = None
    status_id: Optional[int] = None

# Payment Method Schemas

class PaymentMethodCreate(BaseModel):
    method_name: str = Field(max_length=25)

class PaymentMethodOut(BaseModel):
    pmethod_id: int
    method_name: str

    model_config = ConfigDict(from_attributes=True)

# Payment Status Schemas

class PaymentStatusCreate(BaseModel):
    status_name: str = Field(max_length=25)
    
class PaymentStatusOut(BaseModel):
    status_id: int
    status_name: str

    model_config = ConfigDict(from_attributes=True)