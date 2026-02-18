from pydantic import BaseModel


class InvoiceBase(BaseModel):
    sale_id: int
    amount: float


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceResponse(InvoiceBase):
    id: int

    model_config = {
        "from_attributes": True
    }
