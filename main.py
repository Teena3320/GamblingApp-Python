from config.database import engine
from config.logger import logger
from models.user import Base as UserBase
from models.bet import Base as BetBase
from schemas.user_schema import UserCreate
from utils.helpers import build_payload

def init_db():
    UserBase.metadata.create_all(bind=engine)
    BetBase.metadata.create_all(bind=engine)

def main():
    init_db()

    user_input = UserCreate(
        username="teena",
        balance=1000
    )

    payload = build_payload(**user_input.dict())
    logger.info(payload)

if __name__ == "__main__":
    main()