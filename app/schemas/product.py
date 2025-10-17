from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List

# Category Schemas

class CategoryCreate(BaseModel):
    name: str = Field(..., max_length=50)

class CategoryOut(BaseModel):
    cat_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

# Product Schemas

class ProductBase(BaseModel):
    
    name: str = Field(..., max_length=50)
    description: str = Field(..., max_length=300)
    price: float
    stock: int
    image_url: Optional[str] = None
    is_active: Optional[bool] = True
    cat_id: int


class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):

    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=300)
    price: Optional[float] = None
    stock: Optional[int] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = None
    cat_id: Optional[int] = None

class ProductOut(ProductBase):
    product_id: int
    category: Optional[CategoryOut]

    model_config = ConfigDict(from_attributes=True)