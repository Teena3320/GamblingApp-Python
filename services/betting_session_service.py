from config.database import SessionLocal
from models.user import User
from models.betting_preferences import BettingPreferences
from models.betting_session import BettingSession

from services.eligibility_service import EligibilityService
from services.bet_amount_service import BetAmountService
from services.bet_service import BetService
from services.bet_settlement_service import BetSettlementService

from domain.outcome_service import OutcomeService
from domain.analytics.stake_monitor import StakeMonitor


class BettingSessionService:
    """
    UC4: Automated betting session orchestration.
    Coordinates existing services without duplicating logic.
    """

    @staticmethod
    def run_session(gambler_id: int):
        db = SessionLocal()

        user = db.query(User).filter(User.user_id == gambler_id).first()
        prefs = (
            db.query(BettingPreferences)
            .filter(BettingPreferences.gambler_id == gambler_id)
            .first()
        )

        if not user or not prefs:
            db.close()
            raise ValueError("User or betting preferences not found")

        if not prefs.auto_play_enabled:
            db.close()
            raise ValueError("Autoplay is disabled for this gambler")

        max_bets = prefs.max_bets_per_session or float("inf")

        monitor = StakeMonitor(user.current_stake)
        bets_executed = 0

        db.close()

        while bets_executed < max_bets:
            eligible, reason = EligibilityService.is_eligible_to_bet(
                gambler_id=gambler_id
            )

            if not eligible:
                return {
                    "status": "STOPPED",
                    "reason": reason,
                    "bets_executed": bets_executed,
                    "final_stake": monitor.current_stake,
                }

            bet_amount = BetAmountService.calculate_bet_amount(gambler_id)

            bet = BetService.place_bet(user.username, bet_amount)

            outcome = OutcomeService.determine_outcome(win_probability=0.5)

            BetSettlementService.resolve_bet(
                bet_id=bet.bet_id,
                outcome=outcome.value,
            )

            db = SessionLocal()
            user = db.query(User).filter(User.user_id == gambler_id).first()
            monitor.record_stake(user.current_stake)
            db.close()

            bets_executed += 1

        db = SessionLocal()

        session = BettingSession(
            gambler_id=gambler_id,
            strategy=prefs.preferred_strategy,
            start_stake=monitor.initial_stake,
            end_stake=monitor.current_stake,
            total_bets=bets_executed,
            status="COMPLETED" if bets_executed == max_bets else "STOPPED",
        )

        db.add(session)
        db.commit()
        db.close()

        return {
            "status": "COMPLETED",
            "bets_executed": bets_executed,
            "final_stake": monitor.current_stake,
        }
