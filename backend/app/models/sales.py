from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class Sale(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    total_amount: Mapped[float] = mapped_column(Float)
    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"))
