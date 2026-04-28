from decimal import Decimal
from config.database import SessionLocal
from models.user import User
from models.betting_preferences import BettingPreferences
from domain.betting_strategy_type import BettingStrategyType
from services.betting_strategy_factory import BettingStrategyFactory

class BetAmountService:

    @staticmethod
    def calculate_bet_amount(gambler_id: int) -> Decimal:
        db = SessionLocal()

        user = db.query(User).filter(User.user_id == gambler_id).first()
        prefs = (
            db.query(BettingPreferences)
            .filter(BettingPreferences.gambler_id == gambler_id)
            .first()
        )

        if not user or not prefs:
            db.close()
            raise ValueError("User or betting preferences not found")

        strategy_type = BettingStrategyType(prefs.preferred_strategy)

        strategy = BettingStrategyFactory.create(
            strategy_type,
            fixed_amount=prefs.min_bet,
            percentage=Decimal("0.10"),  # example
            base_bet=prefs.min_bet,
        )

        amount = strategy.calculate_bet_amount(
            Decimal(str(user.current_stake))
        )

        db.close()
        return amount