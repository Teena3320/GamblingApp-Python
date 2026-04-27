from decimal import Decimal
from domain.betting_strategy_type import BettingStrategyType

class BettingPreferences:

    def __init__(
        self,
        gambler_id,
        min_bet,
        max_bet,
        preferred_strategy,
        auto_play_enabled,
        max_bets_per_session,
    ):
        self.gambler_id = gambler_id
        self.min_bet = Decimal(str(min_bet))
        self.max_bet = Decimal(str(max_bet))
        self.preferred_strategy = BettingStrategyType(preferred_strategy)
        self.auto_play_enabled = bool(auto_play_enabled)
        self.max_bets_per_session = max_bets_per_session