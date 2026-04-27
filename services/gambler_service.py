from config.database import SessionLocal
from models.user import User
from utils.helpers import recalculate_thresholds

class GamblerService:

    @staticmethod
    def create_gambler(user_data):
        user_data.validate_stake()

        db = SessionLocal()

        existing = (
            db.query(User)
            .filter(User.username == user_data.username)
            .first()
        )

        if existing:
            db.close()
            return existing

        user = User(
            username=user_data.username,
            full_name=user_data.full_name,
            email=user_data.email,
            initial_stake=user_data.initial_stake,
            current_stake=user_data.initial_stake,
            win_threshold=user_data.win_threshold,
            loss_threshold=user_data.loss_threshold,
            min_required_stake=user_data.min_required_stake,
            is_active=True
        )

        db.add(user)
        db.commit()
        db.close()
        return user


    @staticmethod
    def get_by_username(username):
        db = SessionLocal()
        user = db.query(User).filter(User.username == username).first()
        db.close()
        return user

    @staticmethod
    def reset_profile(username):
        db = SessionLocal()
        user = db.query(User).filter(User.username == username).first()

        if not user:
            db.close()
            raise ValueError("Gambler not found")

        win, loss = recalculate_thresholds(
            user.initial_stake,
            user.current_stake,
            user.win_threshold,
            user.loss_threshold
        )

        user.current_stake = user.initial_stake
        user.win_threshold = win
        user.loss_threshold = loss
        user.is_active = True

        db.commit()
        db.close()