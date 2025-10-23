from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List

from app.schemas.product import ProductOut

# Order Detail Schemas

class OrderDetailCreate(BaseModel):
    product_id: int
    quantity: int
    

class OrderDetailOut(BaseModel):
    product_id: int
    order_id: int
    quantity: int
    subtotal: float

    product: Optional[ProductOut]

    model_config = ConfigDict(from_attributes=True)

# Order Schemas

class OrderCreate(BaseModel):
    user_id: int
    items: Optional[List[OrderDetailCreate]] = []
    status_id: int

class OrderOut(BaseModel):
    order_id: int
    created_at: str
    total_amount: float
    user_id: int
    status_id: int
    items: Optional[List[OrderDetailOut]] = []

    model_config = ConfigDict(from_attributes=True)

class OrderUpdate(BaseModel):
    status_id: Optional[int] = None

# Order Status Schemas

class OrderStatusCreate(BaseModel):
    status_name: str = Field(max_length=25)

class OrderStatusOut(BaseModel):
    status_id: int
    status_name: str

    model_config = ConfigDict(from_attributes=True)

