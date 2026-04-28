from decimal import Decimal

class StakeBoundary:
    """
    Defines upper and lower stake boundaries and provides
    evaluation & warning logic.
    """

    def __init__(self, lower_limit, upper_limit):
        if lower_limit < 0:
            raise ValueError("Lower stake limit cannot be negative")

        if upper_limit <= lower_limit:
            raise ValueError("Upper limit must be greater than lower limit")

        self.lower_limit = Decimal(str(lower_limit))
        self.upper_limit = Decimal(str(upper_limit))

        self.lower_warning = self.lower_limit * Decimal("1.2")
        self.upper_warning = self.upper_limit * Decimal("0.8")

    def is_below_lower_limit(self, stake):
        return Decimal(str(stake)) <= self.lower_limit

    def is_above_upper_limit(self, stake):
        return Decimal(str(stake)) >= self.upper_limit

    def is_in_warning_zone(self, stake):
        stake = Decimal(str(stake))
        return (
            self.lower_limit < stake <= self.lower_warning
            or self.upper_warning <= stake < self.upper_limit
        )

    def is_within_bounds(self, stake):
        stake = Decimal(str(stake))
        return self.lower_limit < stake < self.upper_limit
