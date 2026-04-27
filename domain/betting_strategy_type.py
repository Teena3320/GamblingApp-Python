from enum import Enum

class BettingStrategyType(Enum):
    FIXED = "FIXED"
    MARTINGALE = "MARTINGALE"
    ANTI_MARTINGALE = "ANTI_MARTINGALE"
    RANDOM = "RANDOM"