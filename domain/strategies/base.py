from abc import ABC, abstractmethod
from decimal import Decimal


class BettingStrategy(ABC):

    @abstractmethod
    def calculate_bet_amount(self, current_stake: Decimal) -> Decimal:
        pass

    def update_after_win(self):
        pass

    def update_after_loss(self):
        pass

    def reset(self):
        pass