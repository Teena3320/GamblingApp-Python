from decimal import Decimal

from repositories.user_repositories import UserRepository
from repositories.bet_repository import BetRepository
from repositories.stake_transaction_repository import StakeTransactionRepository
from domain.transaction_type import TransactionType


class BetSettlementService:

    @staticmethod
    def resolve_bet(bet_id, outcome):
        bet = BetRepository.get_by_id(bet_id)

        if not bet:
            raise ValueError("Bet not found")

        user = UserRepository.get_by_id(bet["user_id"])

        amount = Decimal(str(bet["amount"]))
        current_stake = Decimal(str(user["current_stake"]))

        if outcome == "WIN":
            payout = amount * 2
            new_stake = current_stake + payout

            UserRepository.update_stake(user["user_id"], new_stake)
            BetRepository.update_status(bet_id, "WON", payout)
            StakeTransactionRepository.create(
                gambler_id=user["user_id"],
                transaction_type=TransactionType.BET_WIN.value,
                amount=payout,
                balance_before=current_stake,
                balance_after=new_stake,
                reference_id=bet_id,
                description="Bet won payout"
            )
        else:
            BetRepository.update_status(bet_id, "LOST", 0)
            StakeTransactionRepository.create(
                gambler_id=user["user_id"],
                transaction_type=TransactionType.BET_LOSS.value,
                amount=Decimal("0"),
                balance_before=current_stake,
                balance_after=current_stake,
                reference_id=bet_id,
                description="Bet lost"
            )