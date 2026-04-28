
from decimal import Decimal
from config.database import SessionLocal
from models.user import User
from models.bet import Bet


class BetService:

    @staticmethod
    def place_bet(username: str, amount):
        db = SessionLocal()

        user = db.query(User).filter(User.username == username).first()
        if not user:
            db.close()
            raise ValueError("User not found")

        if not user.is_active:
            db.close()
            raise ValueError("User is inactive")

        amount = Decimal(str(amount))
        current_stake = Decimal(str(user.current_stake))

        if current_stake < amount:
            db.close()
            raise ValueError("Insufficient balance")

        user.current_stake = current_stake - amount

        bet = Bet(
            user_id=user.user_id,
            amount=amount,
            status="OPEN"
        )

        db.add(bet)
        db.commit()
        db.refresh(bet)          

        bet_id = bet.bet_id       
        db.close()

        return bet_id             
