from decimal import Decimal
from config.database import SessionLocal
from models.bet import Bet
from models.user import User


class BetSettlementService:

    @staticmethod
    def resolve_bet(bet_id: int, outcome: str):
        db = SessionLocal()

        bet = db.query(Bet).filter(Bet.bet_id == bet_id).first()
        if not bet:
            db.close()
            raise ValueError("Bet not found")

        user = db.query(User).filter(User.user_id == bet.user_id).first()
        if not user:
            db.close()
            raise ValueError("User not found")

        outcome = outcome.upper() 

        amount = Decimal(str(bet.amount))
        current_stake = Decimal(str(user.current_stake))

        if outcome == "WIN":
            payout = amount * Decimal("2")
            user.current_stake = current_stake + payout
            bet.status = "WON"
            bet.payout = payout

        elif outcome == "LOSS":
            bet.status = "LOST"
            bet.payout = Decimal("0.00")

        else:
            db.close()
            raise ValueError(f"Invalid outcome: {outcome}")

        db.commit()
        db.close()