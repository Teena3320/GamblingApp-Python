# from config.database import engine
# from models import Base
# from services.betting_session_service import BettingSessionService

# if __name__ == "__main__":
#     Base.metadata.create_all(bind=engine)

#     result = BettingSessionService.run_session(gambler_id=1)
#     print(result)

from config.database import engine
from models import Base
from services.betting_session_service import BettingSessionService


def main():
    # Ensure all tables exist (safe to run multiple times)
    Base.metadata.create_all(bind=engine)

    # Run UC4 betting session
    result = BettingSessionService.run_session(gambler_id=1)

    print("UC4 Result:")
    print(result)


if __name__ == "__main__":
    main()