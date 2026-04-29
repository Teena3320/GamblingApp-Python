from decimal import Decimal
from domain.strategies.base import BettingStrategy


class DAlembertStrategy(BettingStrategy):
    """D'Alembert betting system.

    - unit_bet: fixed betting unit (1 unit)
    - current_bet starts at one unit
    - after a loss: increase bet by one unit
    - after a win: decrease bet by one unit, never below one unit
    """

    def __init__(self, unit_bet, increment=None):
        self.unit_bet = Decimal(str(unit_bet))
        self.increment = Decimal(str(increment)) if increment is not None else Decimal("1")
        self.current_bet = self.unit_bet

        if self.unit_bet <= 0:
            raise ValueError("Unit bet must be positive")
        if self.increment <= 0:
            raise ValueError("Increment must be positive")

    def calculate_bet_amount(self, current_stake: Decimal) -> Decimal:
        return min(self.current_bet, current_stake)

    def update_after_loss(self):
        self.current_bet += self.increment

    def update_after_win(self):
        self.current_bet = max(self.unit_bet, self.current_bet - self.increment)

    def reset(self):
        self.current_bet = self.unit_bet
