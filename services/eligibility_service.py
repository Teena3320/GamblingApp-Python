from decimal import Decimal
from config.database import SessionLocal
from models.user import User
from models.betting_preferences import BettingPreferences
from domain.analytics.stake_boundary import StakeBoundary

class EligibilityService:
    """
    Central eligibility checks for gamblers.
    Pure validation logic using ORM.
    """

    @staticmethod
    def is_eligible_to_bet(gambler_id, requested_bet_amount=None):
        db = SessionLocal()

        user = db.query(User).filter(User.user_id == gambler_id).first()
        if not user:
            db.close()
            return False, "Gambler not found"

        if not user.is_active:
            db.close()
            return False, "Gambler account is inactive"

        current_stake = Decimal(str(user.current_stake))
        min_required_stake = Decimal(str(user.min_required_stake))

        if current_stake < min_required_stake:
            db.close()
            return False, "Current stake below minimum required"

        prefs = (
            db.query(BettingPreferences)
            .filter(BettingPreferences.gambler_id == gambler_id)
            .first()
        )

        if requested_bet_amount is not None and prefs:
            requested_bet_amount = Decimal(str(requested_bet_amount))

            if requested_bet_amount < Decimal(str(prefs.min_bet)):
                db.close()
                return False, "Bet below minimum bet preference"

            if requested_bet_amount > Decimal(str(prefs.max_bet)):
                db.close()
                return False, "Bet exceeds maximum bet preference"

            if requested_bet_amount > current_stake:
                db.close()
                return False, "Insufficient stake for requested bet"

        boundary = StakeBoundary(
            lower_limit=Decimal(str(user.loss_threshold)),
            upper_limit=Decimal(str(user.win_threshold)),
        )

        if boundary.is_below_lower_limit(current_stake):
            db.close()
            return False, "Loss threshold reached"

        db.close()
        return True, "Eligible to bet"