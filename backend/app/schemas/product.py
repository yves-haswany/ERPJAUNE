from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    name: str
    price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None


class ProductResponse(ProductBase):
    id: int
    tenant_id: int

    model_config = {
        "from_attributes": True
    }
