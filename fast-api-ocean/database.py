from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text

# Create a database
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Bright#1270@localhost/dockert'

# Create an engine function
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal function
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
The base from the declarative models that will be created
Catalog from the clases and tables relative to it
"""
Base = declarative_base()

def get_db():
    db = SessionLocal() # Create database session
    try:
        yield db # yield keyword
    finally:
        db.close() # Ensure clossing session