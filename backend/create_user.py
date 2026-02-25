from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db: Session = SessionLocal()

hashed_password = pwd_context.hash("123456")

user = User(
    email="user@example.com",
    hashed_password=hashed_password
)

db.add(user)
db.commit()
db.close()

print("Test user created successfully!")