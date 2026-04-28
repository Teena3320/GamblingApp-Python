from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from models import Base

class Alert(Base):
    __tablename__ = "alerts"

    alert_id = Column(Integer, primary_key=True)
    gambler_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    alert_type = Column(String(50), nullable=False)
    message = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=func.now())