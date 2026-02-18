from sqlalchemy import select
from fastapi import HTTPException
from app.models.sales import Sale
from app.services.inventory_service import adjust_inventory


async def create_sale(db, customer_id: int, total_amount: float, tenant_id: int):
    sale = Sale(
        customer_id=customer_id,
        total_amount=total_amount,
        tenant_id=tenant_id,
    )
    db.add(sale)
    await db.commit()
    await db.refresh(sale)
    return sale


async def list_sales(db, tenant_id: int):
    result = await db.execute(
        select(Sale).where(Sale.tenant_id == tenant_id)
    )
    return result.scalars().all()
