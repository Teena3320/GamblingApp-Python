from decimal import Decimal

from repositories.user_repositories import UserRepository
from repositories.stake_transaction_repository import StakeTransactionRepository
from domain.transaction_type import TransactionType


class UserService:

    @staticmethod
    def register(username, fullname, email, initial_stake, win_threshold, loss_threshold):
        initial_stake = Decimal(str(initial_stake))

        user_id = UserRepository.create(
            username=username,
            fullname=fullname,
            email=email,
            stake=initial_stake,
            win_threshold=win_threshold,
            loss_threshold=loss_threshold
        )

        StakeTransactionRepository.create(
            gambler_id=user_id,
            transaction_type=TransactionType.INITIAL_STAKE.value,
            amount=initial_stake,
            balance_before=initial_stake,
            balance_after=initial_stake,
            description="Initial stake funded"
        )

        return user_id

    @staticmethod
    def login(username):
        user = UserRepository.get_by_username(username)

        if not user:
            return None

        return user["user_id"]