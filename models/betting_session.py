from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, DateTime
from sqlalchemy.sql import func
from models import Base


class BettingSession(Base):
    __tablename__ = "betting_sessions"

    session_id = Column(Integer, primary_key=True)
    gambler_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    strategy = Column(String(50), nullable=False)
    start_stake = Column(Numeric(15, 2), nullable=False)
    end_stake = Column(Numeric(15, 2))
    total_bets = Column(Integer)

    status = Column(String(30), nullable=False)

    started_at = Column(DateTime, default=func.now())
    ended_at = Column(DateTime)