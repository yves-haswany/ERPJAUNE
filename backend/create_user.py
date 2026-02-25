import uuid
import asyncio
from app.core.database import AsyncSessionLocal
from app.models.user import User
from app.models.tenant import Tenant
from passlib.context import CryptContext
from sqlalchemy import select

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user():
    async with AsyncSessionLocal() as session:

        # Get an existing tenant
        tenant = (await session.execute(
            select(Tenant)
        )).scalars().first()

        if not tenant:
            print("No tenant found. Create one first.")
            return

        hashed_password = pwd_context.hash("123456")

        user = User(
            username="admin",
            email="user@example.com",
            hashed_password=hashed_password,
            tenant_id=tenant.id
        )

        session.add(user)
        await session.commit()

        print("User created successfully!")

asyncio.run(create_user())