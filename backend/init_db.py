import asyncio
from app.core.database import engine, Base

# Import ALL models here
from app.models.user import User
from app.models.tenant import Tenant


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())