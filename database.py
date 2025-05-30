from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:SSLWqQEjFBnbGqBFByNFDzaeYXlyszvX@turntable.proxy.rlwy.net:38794/railway")

# Sync SQLAlchemy engine (for table creation, etc.)
engine = create_engine(DATABASE_URL)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# For models
Base = declarative_base()
