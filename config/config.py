import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from typing import Optional
from src.models.student import Student


class Settings(BaseSettings):
    # Database configurations
    DATABASE_URL: Optional[str] = None

    class Config:
        env_file = ".env.dev"
        orm_mode = True


class TestConfig(Settings):
    class TestConfig:
        env_file = ".env.test"
        orm_mode = True


async def initiate_database():
    if os.environ.get("ENV") == "test":
        client = AsyncIOMotorClient(TestConfig().DATABASE_URL)
    else:
        client = AsyncIOMotorClient(Settings().DATABASE_URL)
    db = client.get_default_database()
    await init_beanie(database=db, document_models=[Student])
