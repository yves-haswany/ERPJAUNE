from sqlalchemy import select
from app.models.product import Product


async def create_product(db, name: str, price: float, tenant_id: int):
    product = Product(name=name, price=price, tenant_id=tenant_id)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def list_products(db, tenant_id: int):
    result = await db.execute(
        select(Product).where(Product.tenant_id == tenant_id)
    )
    return result.scalars().all()
