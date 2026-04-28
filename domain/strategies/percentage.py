from decimal import Decimal
from domain.strategies.base import BettingStrategy

class PercentageStrategy(BettingStrategy):

    def __init__(self, percentage):
        self.percentage = Decimal(str(percentage))
        if self.percentage <= 0 or self.percentage > 1:
            raise ValueError("Percentage must be between 0 and 1")

    def calculate_bet_amount(self, current_stake: Decimal) -> Decimal:
        bet_amount = (current_stake * self.percentage).quantize(Decimal("0.01"))

        if bet_amount <= 0:
            raise ValueError("Calculated bet amount invalid")

        return bet_amount