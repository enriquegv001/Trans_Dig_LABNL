import os

from pydantic import BaseSettings, Field

# Validates data to automatically load from environment variables
class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')

settings = Settings()