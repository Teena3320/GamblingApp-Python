from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, ForeignKey

Base = declarative_base()

class Bet(Base):
    __tablename__ = "bets"

    bet_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    amount = Column(Integer, nullable=False)