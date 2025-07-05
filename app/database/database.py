from sqlalchemy import create_engine
from app.core.config import Settings

DATABASE_URL = Settings.DB_CONNECTION

engine = create_engine(DATABASE_URL, echo=True)