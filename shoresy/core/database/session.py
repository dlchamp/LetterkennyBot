from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from shoresy import constants

__all__ = ("SessionLocal",)


SessionLocal = sessionmaker(
    create_async_engine(constants.Config.sqlite_path), expire_on_commit=True, class_=AsyncSession
)
