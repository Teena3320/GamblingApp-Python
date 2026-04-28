from enum import Enum

class BettingStrategyType(Enum):
    FIXED = "FIXED"
    PERCENTAGE = "PERCENTAGE"
    MARTINGALE = "MARTINGALE"
    REVERSE_MARTINGALE = "REVERSE_MARTINGALE"