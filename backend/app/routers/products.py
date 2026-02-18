from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.models.product import Product
from app.dependencies.auth_dependencies import get_current_user
from app.dependencies.db_dependencies import get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
async def list_products(
    current_user=Depends(get_current_user),
    db=Depends(get_db)
):
    result = await db.execute(
        select(Product).where(Product.tenant_id == current_user.tenant_id)
    )
    return result.scalars().all()
