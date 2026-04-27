# from config.database import engine
# from models.user import Base

# Base.metadata.create_all(bind=engine)

# from config.database import engine
# from models.user import Base
# from schemas.user_schema import UserCreate
# from services.gambler_service import GamblerService

# Base.metadata.create_all(bind=engine)

# user = UserCreate(
#     username="sebastian",
#     full_name="Sebastian Teena",
#     email="seb@example.com",
#     initial_stake=1000,
#     win_threshold=1500,
#     loss_threshold=500,
#     min_required_stake=100
# )

# GamblerService.create_gambler(user)
from config.database import engine
from models import Base
from schemas.user_schema import UserCreate
from services.gambler_service import GamblerService
from services.bet_service import BetService

Base.metadata.create_all(bind=engine)

user = UserCreate(
    username="sebastian",
    full_name="Sebastian Teena",
    email="seb@example.com",
    initial_stake=1000,
    win_threshold=1500,
    loss_threshold=500,
    min_required_stake=100
)

GamblerService.create_gambler(user)

BetService.place_bet("sebastian", 200)
BetService.place_bet("sebastian", 300)
