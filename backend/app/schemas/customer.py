from pydantic import BaseModel, EmailStr
from typing import Optional


class CustomerBase(BaseModel):
    name: str
    email: EmailStr


class CustomerCreate(CustomerBase):
    tenant_id: int


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class CustomerResponse(CustomerBase):
    id: int
    tenant_id: int

    model_config = {
        "from_attributes": True
    }
