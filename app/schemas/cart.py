from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import Optional, List

from app.schemas.product import ProductOut

from datetime import datetime, UTC

# Cart Items Schemas

class CartItemCreate(BaseModel):
    cart_id: int
    product_id: int
    unit_price: float
    quantity: int
    subtotal: float = 0.0

    # Validate subtotal after initialization
    @model_validator(mode='after')
    def validate_subtotal(self):
        self.subtotal = self.unit_price * self.quantity
        return self

class CartItemUpdate(BaseModel):
    quantity: Optional[int] = None

class CartItemOut(BaseModel):
    product_id: int
    quantity: int
    subtotal: float

    product: Optional[ProductOut]

    model_config = ConfigDict(from_attributes=True)

# Cart Schemas

class CartCreate(BaseModel):
    created_at: Optional[str] = datetime.now(UTC)
    total_amount: Optional[float] = 0.0
    user_id: int
    status_id: int

class CartOut(BaseModel):
    cart_id: int
    created_at: str
    total_amount: float
    user_id: int
    status_id: int
    items: Optional[List[CartItemOut]] = []

    model_config = ConfigDict(from_attributes=True)

class CartUpdate(BaseModel):
    total_amount: Optional[float] = None
    status_id: Optional[int] = None

# Cart Status Schemas

class CartStatusCreate(BaseModel):
    status_name: str = Field(max_length=25)

class CartStatusOut(BaseModel):
    status_id: int
    status_name: str

    model_config = ConfigDict(from_attributes=True)