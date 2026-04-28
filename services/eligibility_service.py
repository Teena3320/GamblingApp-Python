from decimal import Decimal

from repositories.user_repositories import UserRepository
from repositories.preference_repository import PreferenceRepository
from repositories.alert_repository import AlertRepository
from domain.analytics.stake_boundary import StakeBoundary


class EligibilityService:

    @staticmethod
    def is_eligible_to_bet(user_id, requested_bet_amount=None):
        user = UserRepository.get_by_id(user_id)

        if not user:
            return False, "User not found"

        if not user["is_active"]:
            message = "User inactive"
            AlertRepository.create(user_id, "ELIGIBILITY_FAILURE", message)
            return False, message

        current_stake = Decimal(str(user["current_stake"]))
        min_required = Decimal(str(user["min_required_stake"]))

        if current_stake < min_required:
            message = "Below minimum required stake"
            AlertRepository.create(user_id, "STAKE_TOO_LOW", message)
            return False, message

        prefs = PreferenceRepository.get_by_user_id(user_id)

        if requested_bet_amount is not None and prefs:
            requested_bet_amount = Decimal(str(requested_bet_amount))

            min_bet = Decimal(str(prefs["min_bet"]))
            max_bet = Decimal(str(prefs["max_bet"]))

            if requested_bet_amount < min_bet:
                message = "Below min bet"
                AlertRepository.create(user_id, "BET_SIZE_INVALID", message)
                return False, message

            if requested_bet_amount > max_bet:
                message = "Above max bet"
                AlertRepository.create(user_id, "BET_SIZE_INVALID", message)
                return False, message

            if requested_bet_amount > current_stake:
                message = "Insufficient balance"
                AlertRepository.create(user_id, "INSUFFICIENT_BALANCE", message)
                return False, message

        boundary = StakeBoundary(
            lower_limit=user["loss_threshold"],
            upper_limit=user["win_threshold"],
        )

        if boundary.is_below_lower_limit(current_stake):
            message = "Loss threshold reached"
            AlertRepository.create(user_id, "THRESHOLD_REACHED", message)
            return False, message

        return True, "Eligible"