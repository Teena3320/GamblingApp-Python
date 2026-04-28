from sqlalchemy.orm import declarative_base

Base = declarative_base()

from models.user import User
from models.bet import Bet
from models.stake_transaction import StakeTransaction
from models.betting_preferences import BettingPreferences
from models.betting_session import BettingSession  