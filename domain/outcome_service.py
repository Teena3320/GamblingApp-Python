import random
from domain.betting.enums import BetOutcome


class OutcomeService:
    """
    Determines bet outcome using probability.
    Domain-level logic.
    """

    @staticmethod
    def determine_outcome(win_probability: float) -> BetOutcome:
        if not 0 <= win_probability <= 1:
            raise ValueError("Win probability must be between 0 and 1")

        roll = random.random()

        if roll <= win_probability:
            return BetOutcome.WIN
        else:
            return BetOutcome.LOSS