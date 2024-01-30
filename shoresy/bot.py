from __future__ import annotations

import datetime as dt
import os
import random
import sys as s
from pathlib import Path

import disnake
import sqlalchemy as sa
from disnake import __version__ as disnake_version
from disnake.ext import commands
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.future import select as sa_select

from shoresy import __version__ as bot_version
from shoresy import constants, database, log

logger = log.get_logger(__name__)


class Shoresy(commands.InteractionBot):
    """Base bot instance."""

    def __init__(
        self,
        intents: disnake.Intents,
        *,
        reload: bool,
        activity: disnake.Activity | None = None,
    ) -> None:
        super().__init__(intents=intents, reload=reload, activity=activity)

        self.start_time: dt.datetime = dt.datetime.now(tz=dt.timezone.utc)

        self.engine = engine = create_async_engine(constants.Config.sqlite_path)
        self.db_session = async_sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )

        self.shoresy_responses: list[str] = []
        self.fight_responses: list[str] = []

        self.reload_fight_responses()
        self.reload_shoresy_responses()

    @property
    def db(self) -> async_sessionmaker[AsyncSession]:
        """Return the bot's db AsyncSession."""
        return self.db_session

    def load_responses_from_file(self, path: Path) -> list[str]:
        """Load the responses from the path."""
        with path.open() as f:
            responses = f.readlines()

        logger.info(f"{len(responses)} responses loaded from {path}")
        return responses

    def reload_fight_responses(self) -> None:
        """Reload fight respones from file when cache is empty."""
        path = Path("shoresy/responses/fight.txt")
        self.fight_responses = self.load_responses_from_file(path)

    def reload_shoresy_responses(self) -> None:
        """Reload shoresy responses from file when cache is empty."""
        path = Path("shoresy/responses/shoresy.txt")
        self.fight_responses = self.load_responses_from_file(path)

    def _get_random_shoresy_response(self) -> str:
        """Get a random shoresy response."""
        if not self.shoresy_responses:
            self.reload_shoresy_responses()

        return self.shoresy_responses.pop(
            random.randint(0, (len(self.shoresy_responses) - 1)),
        )

    def get_random_fight_response(self) -> str:
        """Get a random fight trigger response."""
        if not self.shoresy_responses:
            self.reload_fight_responses()

        return self.fight_responses.pop(
            random.randint(0, len(self.fight_responses) - 1),
        )

    async def get_shoresy_response(self, member: disnake.Member) -> str:
        """Get a shoresy response with member and second mentions."""
        response = self._get_random_shoresy_response()
        response = response.format(mention=member.mention)

        if "{second}" in response:
            if not (
                second := await self.get_random_second_member(
                    member.id,
                    member.guild.id,
                )
            ):
                return await self.get_shoresy_response(member)

            response = response.format(second=second.mention)

        return response

    async def on_ready(self) -> None:
        """Execute when bot is ready and cache is populated."""
        now = dt.datetime.now(tz=dt.timezone.utc)
        message = (
            "----------------------------------------------------------------------\n"
            f"Running in DEV MODE: '{constants.DEV_MODE}'\n"
            f'Bot started at: {now.strftime("%m/%d/%Y - %H:%M:%S")}\n'
            f"System Version: {s.version}\n"
            f"Disnake Version: {disnake_version}\n"
            f"Bot Version: {bot_version}\n"
            f"Connected to Discord as {self.user} ({self.user.id})\n"
            "----------------------------------------------------------------------\n"
        )
        logger.info(message)

    def load_extensions(self, path: str) -> None:
        """Load all bot extensions."""
        for item in os.listdir(path):
            if "__" in item or not item.endswith(".py"):
                continue

            ext = f"shoresy.exts.{item[:-3]}"
            super().load_extension(ext)
            logger.info(f"Extension loaded: {item}")

    async def ensure_member(
        self,
        member: disnake.Member,
        *,
        session: AsyncSession | None = None,
    ) -> database.Member:
        """Create or retrieve a member from the database."""
        if not session:
            session = self.db()

        async with session.begin_nested() if session.in_transaction() else session.begin() as trans:
            result = await session.execute(
                sa_select(database.Member)
                .where(database.Member.member_id == member.id)
                .where(database.Member.guild_id == member.guild.id),
            )
            _member = result.scalar_one_or_none()

            if _member is None:
                _member = database.Member(member_id=member.id, guild_id=member.guild.id)

                session.add(_member)
                await trans.commit()

            return _member

    async def remove_member(self, member: disnake.Member, *, all_guilds: bool) -> None:
        """Remove a member form the database."""
        session = self.db()
        query = sa.delete(database.Member).where(database.Member.member_id == member.id)

        if not all_guilds:
            query = query.where(database.Member.guild_id == member.guild.id)

        async with session.begin() as trans:
            await session.execute(query)
            await trans.commit()

    async def get_random_second_member(
        self,
        member_id: int,
        guild_id: int,
    ) -> database.Member | None:
        """Get a random member from the database for the guild_id."""
        session = self.db()

        async with session.begin():
            member = await session.execute(
                sa.select(database.Member)
                .where(
                    database.Member.guild_id == guild_id,
                    database.Member.member_id != member_id,
                )
                .order_by(sa.func.random())
                .limit(1),
            )
            return member.scalar_one_or_none()
