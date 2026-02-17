from sqlalchemy import select
from fastapi import HTTPException
from app.models.inventory import Inventory


async def get_inventory(db, product_id: int):
    result = await db.execute(
        select(Inventory).where(Inventory.product_id == product_id)
    )
    return result.scalar_one_or_none()


async def update_inventory(db, product_id: int, quantity: int):
    inventory = await get_inventory(db, product_id)

    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")

    inventory.quantity = quantity
    await db.commit()
    await db.refresh(inventory)
    return inventory


async def adjust_inventory(db, product_id: int, delta: int):
    inventory = await get_inventory(db, product_id)

    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")

    inventory.quantity += delta
    await db.commit()
    await db.refresh(inventory)
    return inventory
