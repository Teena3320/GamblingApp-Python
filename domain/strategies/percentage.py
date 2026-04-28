from decimal import Decimal
from domain.strategies.base import BettingStrategy


class PercentageStrategy(BettingStrategy):

    def __init__(self, percentage, min_bet=1, max_bet=None):
        self.percentage = Decimal(str(percentage))
        self.min_bet = Decimal(str(min_bet))
        self.max_bet = Decimal(str(max_bet)) if max_bet else None

        if not (Decimal("0") < self.percentage <= Decimal("1")):
            raise ValueError("Percentage must be between 0 and 1")

    def calculate_bet_amount(self, current_stake: Decimal) -> Decimal:
        bet = (current_stake * self.percentage).quantize(Decimal("0.01"))

        if bet < self.min_bet:
            bet = self.min_bet

        if self.max_bet and bet > self.max_bet:
            bet = self.max_bet

        return min(bet, current_stake)