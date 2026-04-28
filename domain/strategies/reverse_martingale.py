from decimal import Decimal
from domain.strategies.base import BettingStrategy


class ReverseMartingaleStrategy(BettingStrategy):

    def __init__(self, base_bet, max_streak=4):
        self.base_bet = Decimal(str(base_bet))
        self.current_bet = self.base_bet
        self.win_streak = 0
        self.max_streak = max_streak

        if self.base_bet <= 0:
            raise ValueError("Base bet must be positive")

    def calculate_bet_amount(self, current_stake: Decimal) -> Decimal:
        return min(self.current_bet, current_stake)

    def update_after_win(self):
        self.win_streak += 1

        if self.win_streak >= self.max_streak:
            self.reset()
        else:
            self.current_bet *= 2

    def update_after_loss(self):
        self.reset()

    def reset(self):
        self.current_bet = self.base_bet
        self.win_streak = 0