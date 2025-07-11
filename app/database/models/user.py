from app.database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func, Boolean


class User(Base):
   __tablename__ = "users"

   user_id = Column(Integer, primary_key=True, index= True)
   username = Column(String(50), unique= True, nullable= False)
   email = Column(String(100), unique=True, nullable=False)
   hashed_password = Column(String, nullable= False)
   created_at = Column(DateTime, default= func.now())
   is_active = Column(Boolean, default= True)

