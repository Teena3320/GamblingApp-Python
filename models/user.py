from sqlalchemy import Column, Integer, String, Boolean, Float
from models import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)

    username = Column(String(100), unique=True, nullable=False)
    full_name = Column(String(255))
    email = Column(String(255))
    is_active = Column(Boolean, default=True)

    initial_stake = Column(Float, nullable=False)
    current_stake = Column(Float, nullable=False)
    win_threshold = Column(Float, nullable=False)
    loss_threshold = Column(Float, nullable=False)
    min_required_stake = Column(Float, nullable=False)
