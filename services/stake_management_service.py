from decimal import Decimal
from config.database import SessionLocal
from models.user import User
from models.stake_transaction import StakeTransaction
from domain.transaction_type import TransactionType

class StakeManagementService:

    @staticmethod
    def record_transaction(
        gambler_id,
        transaction_type: TransactionType,
        amount,
        reference_id=None,
        description=None,
    ):
        amount = Decimal(str(amount))
        db = SessionLocal()

        user = db.query(User).filter(User.user_id == gambler_id).first()
        if not user:
            db.close()
            raise ValueError("Gambler not found")

        balance_before = Decimal(str(user.current_stake))

        if transaction_type in (
            TransactionType.BET_LOSS,
            TransactionType.WITHDRAWAL,
        ):
            balance_after = balance_before - amount
        else:
            balance_after = balance_before + amount

        if balance_after < 0:
            db.close()
            raise ValueError("Resulting stake cannot be negative")

        tx = StakeTransaction(
            gambler_id=gambler_id,
            transaction_type=transaction_type.value,
            amount=amount,
            balance_before=balance_before,
            balance_after=balance_after,
            reference_id=reference_id,
            description=description,
        )

        user.current_stake = balance_after

        db.add(tx)
        db.commit()
        db.close()