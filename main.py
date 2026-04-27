from config.database import engine, SessionLocal
from models import Base
from models.bet import Bet
from models.user import User
from services.bet_settlement_service import BetSettlementService

def main():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # ✅ Ensure a user exists (Feature 1 prerequisite)
    user = db.query(User).filter(User.username == "sebastian").first()
    if not user:
        user = User(
            username="sebastian",
            full_name="Sebastian Teena",
            email="seb@example.com",
            initial_stake=1000,
            current_stake=800,
            win_threshold=1500,
            loss_threshold=500,
            min_required_stake=100,
            is_active=True,
        )
        db.add(user)
        db.commit()

    # ✅ Ensure an OPEN bet exists
    bet = db.query(Bet).filter(Bet.status == "OPEN").first()
    if not bet:
        bet = Bet(
            user_id=user.user_id,
            amount=200,
            status="OPEN",
        )
        db.add(bet)
        db.commit()

    bet_id = bet.bet_id
    db.close()

    # ✅ Feature 2: resolve bet
    BetSettlementService.resolve_bet(
        bet_id=bet_id,
        outcome="WIN",
    )

    print(f"Bet {bet_id} resolved as WIN")

if __name__ == "__main__":
    main()