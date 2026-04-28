from decimal import Decimal
from domain.strategies.base import BettingStrategy

class MartingaleStrategy(BettingStrategy):

    def __init__(self, base_bet):
        self.base_bet = Decimal(str(base_bet))
        self.current_bet = self.base_bet

        if self.base_bet <= 0:
            raise ValueError("Base bet must be positive")

    def calculate_bet_amount(self, current_stake: Decimal) -> Decimal:
        if self.current_bet > current_stake:
            raise ValueError("Insufficient stake for Martingale strategy")

        return self.current_bet

    def update_after_loss(self):
        self.current_bet *= 2

    def reset(self):
        self.current_bet = self.base_bet
