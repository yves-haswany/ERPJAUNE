from sqlalchemy import select
from app.models.invoice import Invoice


async def create_invoice(db, sale_id: int, amount: float):
    invoice = Invoice(
        sale_id=sale_id,
        amount=amount,
    )
    db.add(invoice)
    await db.commit()
    await db.refresh(invoice)
    return invoice


async def get_invoice(db, invoice_id: int):
    result = await db.execute(
        select(Invoice).where(Invoice.id == invoice_id)
    )
    return result.scalar_one_or_none()
