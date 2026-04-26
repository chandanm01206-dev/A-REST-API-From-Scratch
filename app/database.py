from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# create_engine connects to the database
# connect_args={"check_same_thread": False} is ONLY needed for SQLite in FastAPI
engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal is responsible for executing queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the parent class for all our Database Models
Base = declarative_base()
