from sqlalchemy import select
from app.models.tenant import Tenant


async def create_tenant(db, name: str):
    tenant = Tenant(name=name)
    db.add(tenant)
    await db.commit()
    await db.refresh(tenant)
    return tenant


async def get_tenant(db, tenant_id: int):
    result = await db.execute(select(Tenant).where(Tenant.id == tenant_id))
    return result.scalar_one_or_none()


async def list_tenants(db):
    result = await db.execute(select(Tenant))
    return result.scalars().all()
