from sqlalchemy import delete, exc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func

from shoresy.core.database import models


async def add_member(session: AsyncSession, *, member_id: int, guild_id: int) -> None:
    """Adds a new member to that database if they do not already exist"""

    async with session() as session:
        resp = await session.execute(
            select(models.Member)
            .where(models.Member.member_id == member_id)
            .where(models.Member.guild_id == guild_id)
        )
        member = resp.scalars().first()

        if member:
            return

        try:
            session.add(models.Member(member_id=member_id, guild_id=guild_id))
        except exc.IntegrityError:
            session.rollback()
            raise

        else:
            await session.commit()


async def remove_member(session: AsyncSession, *, member_id: int) -> None:
    """Removes the member from the database for the guild"""

    async with session() as session:
        await session.execute(delete(models.Member).where(models.Member.member_id == member_id))

        await session.commit()


async def get_random_member(
    session: AsyncSession, *, member_id: int, guild_id: int
) -> models.Member:
    """Get all member IDs for the guild from the database and return
    a randomly selected ID that is NOT the member_id"""

    async with session() as session:
        result = await session.execute(
            select(models.Member)
            .where(models.Member.guild_id == guild_id)
            .where(models.Member.member_id != member_id)
            .order_by(func.random())
            .limit(1)
        )
        return result.scalars().first()
