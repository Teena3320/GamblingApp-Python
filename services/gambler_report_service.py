from decimal import Decimal
from sqlalchemy import func

from config.database import SessionLocal
from models.user import User
from models.betting_session import BettingSession
from models.stake_transaction import StakeTransaction
from domain.analytics.gambler_report import GamblerReport


class GamblerReportService:
    """
    UC5: Aggregates historical gambling analytics.
    Read-only service.
    """

    @staticmethod
    def generate_report(gambler_id: int) -> GamblerReport:
        db = SessionLocal()

        user = db.query(User).filter(User.user_id == gambler_id).first()
        if not user:
            db.close()
            raise ValueError("Gambler not found")

        total_sessions = (
            db.query(func.count(BettingSession.session_id))
            .filter(BettingSession.gambler_id == gambler_id)
            .scalar()
        )

        total_bets = (
            db.query(func.sum(BettingSession.total_bets))
            .filter(BettingSession.gambler_id == gambler_id)
            .scalar()
            or 0
        )

        transactions = (
            db.query(StakeTransaction)
            .filter(StakeTransaction.gambler_id == gambler_id)
            .all()
        )

        net_pnl = Decimal("0.00")
        highest = user.initial_stake
        lowest = user.initial_stake

        for tx in transactions:
            net_pnl += tx.balance_after - tx.balance_before
            highest = max(highest, tx.balance_after)
            lowest = min(lowest, tx.balance_after)

        report = GamblerReport(
            total_sessions=total_sessions,
            total_bets=total_bets,
            net_profit_loss=net_pnl,
            highest_stake=highest,
            lowest_stake=lowest,
            final_stake=user.current_stake,
        )

        db.close()
        return report