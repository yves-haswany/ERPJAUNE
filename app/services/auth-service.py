from sqlalchemy import select
from fastapi import HTTPException
from app.models.user import User
from app.core.security import verify_password, create_access_token


async def authenticate_user(db, email: str, password: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return user


async def login_user(db, email: str, password: str):
    user = await authenticate_user(db, email, password)

    token = create_access_token({"sub": str(user.id)})
    return {
        "access_token": token,
        "token_type": "bearer",
    }
