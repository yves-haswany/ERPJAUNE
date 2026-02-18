from pydantic import BaseModel
from typing import Optional


class SaleBase(BaseModel):
    customer_id: int
    total_amount: float


class SaleCreate(SaleBase):
    tenant_id: int


class SaleResponse(SaleBase):
    id: int
    tenant_id: int

    model_config = {
        "from_attributes": True
    }
