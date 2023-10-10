from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Environment variables
POSTGRESQL_PASSWORD=os.getenv("POSTGRESQL_PASSWORD")

class Config:
    # This display additional information on the Terminal
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://admin:{POSTGRESQL_PASSWORD}@localhost:5432/ksprojects"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
