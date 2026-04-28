from decimal import Decimal

from repositories.user_repositories import UserRepository
from repositories.bet_repository import BetRepository
from repositories.stake_transaction_repository import StakeTransactionRepository
from services.eligibility_service import EligibilityService
from domain.transaction_type import TransactionType


class BetService:

    @staticmethod
    def place_bet(user_id, amount):
        eligible, reason = EligibilityService.is_eligible_to_bet(user_id, requested_bet_amount=amount)
        if not eligible:
            raise ValueError(f"Cannot place bet: {reason}")

        user = UserRepository.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        current_stake = Decimal(str(user["current_stake"]))
        amount = Decimal(str(amount))

        if current_stake < amount:
            raise ValueError("Insufficient balance")

        bet_id = BetRepository.create(user_id, amount)

        new_stake = current_stake - amount
        UserRepository.update_stake(user_id, new_stake)

        StakeTransactionRepository.create(
            gambler_id=user_id,
            transaction_type=TransactionType.BET_PLACED.value,
            amount=amount,
            balance_before=current_stake,
            balance_after=new_stake,
            reference_id=bet_id,
            description="Bet placed"
        )

        return bet_id