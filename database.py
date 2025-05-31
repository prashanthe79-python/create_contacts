from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://create_contacts_ef84_user:JgJ9yWGhbtwhI5eKT7Rinq6wuKPjSZwq@dpg-d0tc4lidbo4c739h6980-a/create_contacts_ef84")

# Sync SQLAlchemy engine (for table creation, etc.)
engine = create_engine(DATABASE_URL)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# For models
Base = declarative_base()
