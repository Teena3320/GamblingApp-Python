from config.database import engine
from models import Base
from services.betting_session_service import BettingSessionService


def main():
    Base.metadata.create_all(bind=engine)

    result = BettingSessionService.run_session(gambler_id=1)

    print("Session Result:")
    print(result)


if __name__ == "__main__":
    main()