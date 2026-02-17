from sqlalchemy import select
from app.models.user import User
from app.core.security import get_password_hash


async def create_user(db, email: str, password: str, tenant_id: int):
    user = User(
        email=email,
        hashed_password=get_password_hash(password),
        tenant_id=tenant_id,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user(db, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def list_users_by_tenant(db, tenant_id: int):
    result = await db.execute(
        select(User).where(User.tenant_id == tenant_id)
    )
    return result.scalars().all()
