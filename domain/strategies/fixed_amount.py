from decimal import Decimal
from domain.strategies.base import BettingStrategy

class FixedAmountStrategy(BettingStrategy):
    def calculate_bet_amount(self, current_stake: Decimal) -> Decimal:
        return min(self.fixed_amount, current_stake)
    def __init__(self, fixed_amount):
        self.fixed_amount = Decimal(str(fixed_amount))
        if self.fixed_amount <= 0:
            raise ValueError("Fixed bet amount must be positive")