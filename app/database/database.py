from sqlalchemy import create_engine
from app.core.config import Settings
from sqlalchemy.orm import declarative_base

settings = Settings()
DATABASE_URL = Settings.DB_CONNECTION

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

