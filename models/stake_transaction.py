from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from models import Base

class StakeTransaction(Base):
    __tablename__ = "stake_transactions"

    transaction_id = Column(Integer, primary_key=True)
    gambler_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    transaction_type = Column(String(30), nullable=False)

    amount = Column(Numeric(15, 2), nullable=False)
    balance_before = Column(Numeric(15, 2), nullable=False)
    balance_after = Column(Numeric(15, 2), nullable=False)

    reference_id = Column(Integer)
    description = Column(String(255))
