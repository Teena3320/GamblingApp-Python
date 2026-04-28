from sqlalchemy import Column, Integer, ForeignKey, Boolean, Numeric, String
from models import Base

class BettingPreferences(Base):
    __tablename__ = "betting_preferences"

    preference_id = Column(Integer, primary_key=True)
    gambler_id = Column(Integer, ForeignKey("users.user_id"), unique=True, nullable=False)

    min_bet = Column(Numeric(15, 2), nullable=False)
    max_bet = Column(Numeric(15, 2), nullable=False)

    preferred_strategy = Column(String(50), nullable=False)
    auto_play_enabled = Column(Boolean, default=False)
    max_bets_per_session = Column(Integer)
