from sqlalchemy import select, func
from app.models.sales import Sale
from app.models.product import Product


async def total_sales_by_tenant(db, tenant_id: int):
    result = await db.execute(
        select(func.sum(Sale.total_amount)).where(
            Sale.tenant_id == tenant_id
        )
    )
    return result.scalar() or 0


async def total_products_by_tenant(db, tenant_id: int):
    result = await db.execute(
        select(func.count(Product.id)).where(
            Product.tenant_id == tenant_id
        )
    )
    return result.scalar() or 0
