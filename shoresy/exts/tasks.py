import sqlalchemy as sa
import disnake
from disnake.ext import plugins as p
from disnake.ext import tasks

from shoresy import database
from shoresy.bot import Shoresy

plugin = p.Plugin[Shoresy]()


@plugin.register_loop(wait_until_ready=True)
@tasks.loop(minutes=1)
async def set_activity() -> None:
    """Set activity after bot is ready."""

    activity = disnake.Activity(
        type=disnake.ActivityType.custom,
        name="custom",
        state=f"Chirping in {len(plugin.bot.guilds)} guilds!",
    )
    await plugin.bot.change_presence(activity=activity)


@plugin.register_loop(wait_until_ready=True)
@tasks.loop(count=1)
async def sync_database_members():
    '''Ensure all members in the db are only members from current guilds.'''
    guild_ids = [guild.id for guild in plugin.bot.guilds]
    member_ids = set([m.id for guild in plugin.bot.guilds for m in guild.members])


    session = plugin.bot.db()

    async with session.begin() as trans:
        await session.execute(sa.delete(database.Member).where(database.Member.guild_id.not_in(guild_ids)))
        await session.execute(sa.delete(database.Member).where(database.Member.id.not_in(member_ids)))
        await trans.commit()



setup, teardown = plugin.create_extension_handlers()
