from config.database import SessionLocal
from models.user import User
from models.bet import Bet

class BetService:

    @staticmethod
    def place_bet(username: str, amount: int):
        db = SessionLocal()

        user = db.query(User).filter(User.username == username).first()
        if not user:
            db.close()
            raise ValueError("User not found")

        if not user.is_active:
            db.close()
            raise ValueError("User is inactive")

        if user.current_stake < amount:
            db.close()
            raise ValueError("Insufficient balance")

        user.current_stake -= amount

        bet = Bet(
            user_id=user.user_id,
            amount=amount
        )

        db.add(bet)

        if user.current_stake <= user.loss_threshold:
            user.is_active = False

        if user.current_stake >= user.win_threshold:
            user.is_active = False

        db.commit()
        db.close()

        return bet