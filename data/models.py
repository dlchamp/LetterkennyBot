from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Our Model class holds table name and column definitions
Base = declarative_base()


class Members(Base):
    """
    Class that represents the 'members' table
    """

    __tablename__ = "members"

    id: int = Column(Integer, primary_key=True)
    guild_id: int = Column(BigInteger, nullable=False, unique=False)
    member_id: int = Column(BigInteger, nullable=False, unique=False)


engine = create_async_engine("sqlite+aiosqlite:///data/data.db")


async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


if __name__ == "__main__":
    from asyncio import run

    run(main())
