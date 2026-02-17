from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from app.schemas.auth import LoginRequest, TokenResponse
from app.models.user import User
from app.core.security import verify_password
from app.core.auth import create_access_token
from app.dependencies.db_dependencies import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest, db=Depends(get_db)):
    result = await db.execute(
        select(User).where(User.username == data.username)
    )
    user = result.scalar_one_or_none()

    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({
        "user_id": str(user.id),
        "tenant_id": str(user.tenant_id)
    })

    return {"access_token": token}
