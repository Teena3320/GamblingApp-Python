from config.database import SessionLocal
from models.user import User
from models.bet import Bet

class BetSettlementService:

    @staticmethod
    def resolve_bet(bet_id: int, outcome: str):
        db = SessionLocal()

        bet = db.query(Bet).filter(Bet.bet_id == bet_id).first()
        if not bet:
            db.close()
            raise ValueError("Bet not found")

        if bet.status != "OPEN":
            db.close()
            raise ValueError("Bet already settled")

        user = db.query(User).filter(User.user_id == bet.user_id).first()

        if outcome == "WIN":
            winnings = bet.amount * 2
            user.current_stake += winnings
            bet.payout = winnings
            bet.status = "WON"
        elif outcome == "LOSE":
            bet.payout = 0
            bet.status = "LOST"
        else:
            db.close()
            raise ValueError("Invalid outcome")

        db.commit()
        db.close()