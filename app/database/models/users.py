from database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func

class User(Base):
   __tablename__ = "users"

   user_id = Column(Integer, primary_key=True)
   username = Column(String(50))
   email = Column(String(100))
   hashed_password = Column(String)
   created_at = Column(DateTime, default= func.now())

