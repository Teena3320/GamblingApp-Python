from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DB_URL

engine = create_engine(DB_URL, echo=False)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)