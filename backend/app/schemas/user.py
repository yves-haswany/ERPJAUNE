from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str
    tenant_id: int


class UserResponse(UserBase):
    id: int
    tenant_id: int

    model_config = {
        "from_attributes": True
    }
