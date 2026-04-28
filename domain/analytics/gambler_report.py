from decimal import Decimal

class GamblerReport:
    """
    Read-only analytics report for a gambler.
    """

    def __init__(
        self,
        total_sessions,
        total_bets,
        net_profit_loss,
        highest_stake,
        lowest_stake,
        final_stake,
    ):
        self.total_sessions = total_sessions
        self.total_bets = total_bets
        self.net_profit_loss = Decimal(str(net_profit_loss))
        self.highest_stake = Decimal(str(highest_stake))
        self.lowest_stake = Decimal(str(lowest_stake))
        self.final_stake = Decimal(str(final_stake))

    def summary(self):
        return {
            "total_sessions": self.total_sessions,
            "total_bets": self.total_bets,
            "net_profit_loss": self.net_profit_loss,
            "highest_stake": self.highest_stake,
            "lowest_stake": self.lowest_stake,
            "final_stake": self.final_stake,
        }