import os
from dotenv import load_dotenv 
load_dotenv()

class Settings:
   JWT_SECRET_KEY = os.getenv("SECRET_KEY")
   DB_CONNECTION = os.getenv("DATABASE_CONNECTION")
   TOKEN_EXP_DATE = int(os.getenv("TOKEN_EXPIRATION_DATE"))
   HASHING_ALGORITHM = os.getenv("HASHING_ALGORITHM")
   