from decimal import Decimal
from domain.strategies.base import BettingStrategy


class FibonacciStrategy(BettingStrategy):
    def __init__(self, unit_bet, max_bet=None, max_steps=12):
        self.unit_bet = Decimal(str(unit_bet))
        self.max_bet = Decimal(str(max_bet)) if max_bet is not None else None
        self.sequence = [Decimal("1"), Decimal("1")]
        self.index = 0
        self.max_steps = int(max_steps)

        if self.unit_bet <= 0:
            raise ValueError("Unit bet must be positive")
        if self.max_steps < 2:
            raise ValueError("max_steps must be at least 2")
        if self.max_bet is not None and self.max_bet <= 0:
            raise ValueError("Max bet must be positive")

    def calculate_bet_amount(self, current_stake: Decimal) -> Decimal:
        self._ensure_sequence_index()
        amount = self.unit_bet * self.sequence[self.index]
        if self.max_bet is not None:
            amount = min(amount, self.max_bet)
        return min(amount, current_stake)

    def update_after_loss(self):
        if self.index < self.max_steps - 1:
            self.index += 1
        self._ensure_sequence_index()

    def update_after_win(self):
        if self.index < self.max_steps - 1:
            self.index += 1
        self._ensure_sequence_index()

    def reset(self):
        self.index = 0

    def _ensure_sequence_index(self):
        while len(self.sequence) <= self.index and len(self.sequence) < self.max_steps:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])