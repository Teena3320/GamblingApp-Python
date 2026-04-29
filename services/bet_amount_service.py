from decimal import Decimal

from repositories.user_repositories import UserRepository
from repositories.preference_repository import PreferenceRepository

from domain.betting_strategy_type import BettingStrategyType
from services.betting_strategy_factory import BettingStrategyFactory


class BetAmountService:

    @staticmethod
    def validate_manual_bet(user_id, raw_value):
        user = UserRepository.get_by_id(user_id)
        prefs = PreferenceRepository.get_by_user_id(user_id)

        if not user or not prefs:
            raise ValueError("User or preferences not found")

        strategy_type = BettingStrategyType(prefs["preferred_strategy"])
        current_stake = Decimal(str(user["current_stake"]))
        min_bet = Decimal(str(prefs["min_bet"]))
        max_bet = Decimal(str(prefs["max_bet"]))

        if strategy_type == BettingStrategyType.PERCENTAGE:
            percentage = Decimal(str(raw_value))
            if percentage <= 0 or percentage > 100:
                raise ValueError("Percentage must be between 0 and 100")
            amount = (current_stake * percentage / Decimal("100")).quantize(Decimal("0.01"))
        else:
            amount = Decimal(str(raw_value))

        if amount < min_bet:
            raise ValueError(f"Bet amount must be at least {min_bet}")
        if amount > max_bet:
            raise ValueError(f"Bet amount must be at most {max_bet}")
        if amount > current_stake:
            raise ValueError("Insufficient balance")

        return amount

    @staticmethod
    def calculate_bet_amount(user_id):
        user = UserRepository.get_by_id(user_id)
        prefs = PreferenceRepository.get_by_user_id(user_id)

        if not user or not prefs:
            raise ValueError("User or preferences not found")

        strategy_type = BettingStrategyType(prefs["preferred_strategy"])

        base_bet = Decimal(str(prefs["min_bet"]))

        strategy = BettingStrategyFactory.create(
            strategy_type,
            fixed_amount=prefs["min_bet"],
            percentage=Decimal("0.1"),
            base_bet=base_bet,
            max_bet=Decimal(str(prefs["max_bet"])) if strategy_type == BettingStrategyType.FIBONACCI else None,
            increment=Decimal(str(prefs["min_bet"])),
        )

        current_stake = Decimal(str(user["current_stake"]))

        return strategy.calculate_bet_amount(current_stake)