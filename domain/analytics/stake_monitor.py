from decimal import Decimal


class StakeMonitor:
    """
    Tracks stake movement during a betting session.
    Provides analytics like peak, lowest, and volatility.
    """

    def __init__(self, initial_stake):
        self.initial_stake = Decimal(str(initial_stake))
        self.current_stake = self.initial_stake

        self.peak_stake = self.initial_stake
        self.lowest_stake = self.initial_stake

        self.history = [self.initial_stake]

    def record_stake(self, new_stake):
        new_stake = Decimal(str(new_stake))

        self.current_stake = new_stake
        self.history.append(new_stake)

        if new_stake > self.peak_stake:
            self.peak_stake = new_stake

        if new_stake < self.lowest_stake:
            self.lowest_stake = new_stake

    def get_volatility(self):
        """
        Volatility = total absolute change between consecutive stakes.
        """
        if len(self.history) < 2:
            return Decimal("0.00")

        volatility = Decimal("0.00")
        for i in range(1, len(self.history)):
            volatility += abs(self.history[i] - self.history[i - 1])

        return volatility

    def summary(self):
        return {
            "initial_stake": self.initial_stake,
            "current_stake": self.current_stake,
            "peak_stake": self.peak_stake,
            "lowest_stake": self.lowest_stake,
            "volatility": self.get_volatility(),
            "changes_count": len(self.history) - 1,
        }