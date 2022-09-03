from random import choice, choices

from sqlalchemy import delete
from sqlalchemy.future import select

from data.models import Members, async_session

# from models import Members, async_session


async def add_member(member_id: int, guild_id: int) -> None:
    """Adds a new member to that database if they do not already exist"""

    async with async_session() as session:
        async with session.begin():

            result = await session.execute(
                select(Members)
                .where(Members.member_id == member_id)
                .where(Members.guild_id == guild_id)
            )

            member = result.scalars().first()

            if member is None:
                session.add(Members(member_id=member_id, guild_id=guild_id))
                await session.commit()


async def remove_member(member_id: int, guild_id: int, *, all_guilds: bool) -> None:
    """Removes the member from the database for the guild"""
    if all_guilds:
        statement = delete(Members).where(Members.member_id == member_id)
    else:
        statement = (
            delete(Members)
            .where(Members.member_id == member_id)
            .where(Members.guild_id == guild_id)
        )

    async with async_session() as session:
        async with session.begin():

            await session.execute(statement)


async def get_random_member(member_id: int, guild_id: int) -> int:
    """Get all member IDs for the guild from the database and return
    a randomly selected ID that is NOT the member_id"""

    async with async_session() as session:
        async with session.begin():

            result = await session.execute(
                select(Members).where(Members.guild_id == guild_id)
            )

    members: list[int] = [
        r.member_id for r in result.scalars() if r.member_id != member_id
    ]
    if members != []:
        selection: list[int] = choices(members)
        return choice(selection)


if __name__ == "__main__":
    import asyncio

    asyncio.run(remove_member(173105961442082816, 947543739671412878))
