from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create engine for SQLite
engine = create_engine("sqlite:///playlist.db")

# Base class for models
Base = declarative_base()

# Session
Session = sessionmaker(bind=engine)
session = Session()
