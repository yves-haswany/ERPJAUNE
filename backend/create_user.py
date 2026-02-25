import asyncio
from app.core.database import AsyncSessionLocal
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user():
    async with AsyncSessionLocal() as session:
        hashed_password = pwd_context.hash("123456")

        user = User(
            email="user@example.com",
            hashed_password=hashed_password
        )

        session.add(user)
        await session.commit()

    print("✅ Test user created successfully!")


if __name__ == "__main__":
    asyncio.run(create_user())