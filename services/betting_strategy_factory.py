from decimal import Decimal
from domain.betting_strategy_type import BettingStrategyType
from domain.strategies.fixed_amount import FixedAmountStrategy
from domain.strategies.percentage import PercentageStrategy
from domain.strategies.martingale import MartingaleStrategy
from domain.strategies.reverse_martingale import ReverseMartingaleStrategy
from domain.strategies.fibonacci import FibonacciStrategy
from domain.strategies.d_alembert import DAlembertStrategy

class BettingStrategyFactory:

    @staticmethod
    def create(strategy_type: BettingStrategyType, **kwargs):
        if strategy_type == BettingStrategyType.FIXED:
            return FixedAmountStrategy(kwargs["fixed_amount"])

        if strategy_type == BettingStrategyType.PERCENTAGE:
            return PercentageStrategy(kwargs["percentage"])

        if strategy_type == BettingStrategyType.MARTINGALE:
            return MartingaleStrategy(kwargs["base_bet"])

        if strategy_type == BettingStrategyType.REVERSE_MARTINGALE:
            return ReverseMartingaleStrategy(kwargs["base_bet"])

        if strategy_type == BettingStrategyType.FIBONACCI:
            return FibonacciStrategy(kwargs["base_bet"], max_bet=kwargs.get("max_bet"))

        if strategy_type == BettingStrategyType.D_ALEMBERT:
            return DAlembertStrategy(kwargs["base_bet"], kwargs.get("increment", kwargs["base_bet"]))

        raise ValueError(f"Unsupported strategy: {strategy_type}")
