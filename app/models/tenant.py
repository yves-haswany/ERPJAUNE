import uuid
from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.core.database import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    legal_name = Column(String)
    country = Column(String)
    city = Column(String)
    currency = Column(String)
    timezone = Column(String)
    features = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)
