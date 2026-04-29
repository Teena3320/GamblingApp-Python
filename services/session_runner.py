from decimal import Decimal

from services.eligibility_service import EligibilityService
from services.bet_service import BetService
from services.bet_settlement_service import BetSettlementService

from repositories.user_repositories import UserRepository
from repositories.preference_repository import PreferenceRepository
from repositories.betting_session_repository import BettingSessionRepository

from domain.outcome_service import OutcomeService
from domain.betting_strategy_type import BettingStrategyType
from services.betting_strategy_factory import BettingStrategyFactory


class SessionRunner:

    @staticmethod
    def run(user_id, rounds=10):
        results = []

        user = UserRepository.get_by_id(user_id)
        prefs = PreferenceRepository.get_by_user_id(user_id)

        strategy_type = BettingStrategyType(prefs["preferred_strategy"])
        max_bet = Decimal(str(prefs["max_bet"]))

        base_bet = Decimal(str(prefs["min_bet"]))

        strategy = BettingStrategyFactory.create(
            strategy_type,
            fixed_amount=prefs["min_bet"],
            percentage=Decimal("0.1"),
            base_bet=base_bet,
            max_bet=max_bet,
            increment=Decimal(str(prefs["min_bet"])),
        )

        session_id = BettingSessionRepository.create_session(
            gambler_id=user_id,
            strategy=prefs["preferred_strategy"],
            start_stake=Decimal(str(user["current_stake"]))
        )

        for _ in range(rounds):

            eligible, reason = EligibilityService.is_eligible_to_bet(user_id)
            if not eligible:
                BettingSessionRepository.finish_session(
                    session_id=session_id,
                    end_stake=Decimal(str(UserRepository.get_by_id(user_id)["current_stake"])),
                    total_bets=len(results),
                    status="STOPPED"
                )
                return {
                    "status": "STOPPED",
                    "reason": reason,
                    "results": results
                }

            user = UserRepository.get_by_id(user_id)
            current_stake = Decimal(str(user["current_stake"]))

            amount = strategy.calculate_bet_amount(current_stake)

            bet_id = BetService.place_bet(user_id, amount)

            outcome = OutcomeService.determine_outcome(0.5)

            BetSettlementService.resolve_bet(bet_id, outcome.value)

            if outcome.value == "WIN":
                strategy.update_after_win()
            else:
                strategy.update_after_loss()

            results.append({
                "bet": float(amount),
                "result": outcome.value
            })

        BettingSessionRepository.finish_session(
            session_id=session_id,
            end_stake=Decimal(str(UserRepository.get_by_id(user_id)["current_stake"])),
            total_bets=len(results),
            status="COMPLETED"
        )

        return {
            "status": "COMPLETED",
            "results": results
        }