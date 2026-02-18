from pydantic import BaseModel


class TenantBase(BaseModel):
    name: str


class TenantCreate(TenantBase):
    pass


class TenantResponse(TenantBase):
    id: int

    model_config = {
        "from_attributes": True
    }
