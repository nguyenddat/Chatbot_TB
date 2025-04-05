import os
from typing import *

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base

load_dotenv()

# engine = create_engine(os.getenv("DB_URL"), pool_pre_ping=True)
# Base.metadata.create_all(bind=engine)

engine = create_engine("sqlite:///chatbot.db", echo=True)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()