
import random
from domain.transaction_type import TransactionType


class OutcomeService:
    """
    Determines the outcome of a bet using probability.
    Pure domain logic. No DB access.
    """

    @staticmethod
    def determine_outcome(win_probability: float):
        if win_probability < 0 or win_probability > 1:
            raise ValueError("Win probability must be between 0 and 1")

        roll = random.random()  # value between 0.0 and 1.0

        if roll <= win_probability:
            return TransactionType.BET_WIN
        else:
            return TransactionType.BET_LOSS
