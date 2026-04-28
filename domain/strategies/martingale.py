from decimal import Decimal
from domain.strategies.base import BettingStrategy


class MartingaleStrategy(BettingStrategy):

    def __init__(self, base_bet, max_multiplier=16):
        self.base_bet = Decimal(str(base_bet))
        self.current_bet = self.base_bet
        self.max_multiplier = Decimal(str(max_multiplier))

        if self.base_bet <= 0:
            raise ValueError("Base bet must be positive")

    def calculate_bet_amount(self, current_stake: Decimal) -> Decimal:
        bet = min(self.current_bet, current_stake)
        return bet

    def update_after_loss(self):
        next_bet = self.current_bet * 2

        # cap growth (critical fix)
        if next_bet > self.base_bet * self.max_multiplier:
            self.reset()
        else:
            self.current_bet = next_bet

    def update_after_win(self):
        self.reset()

    def reset(self):
        self.current_bet = self.base_bet