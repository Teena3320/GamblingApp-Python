from sqlalchemy import Column, Integer, ForeignKey
from models import Base

class Bet(Base):
    __tablename__ = "bets"

    bet_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    amount = Column(Integer, nullable=False)