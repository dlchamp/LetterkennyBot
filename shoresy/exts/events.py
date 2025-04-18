import disnake
from disnake.ext import plugins as p

from shoresy import log
from shoresy.bot import Shoresy

plugin = p.Plugin[Shoresy]()
logger = log.get_logger(__name__)


@plugin.listener()
async def on_guild_join(guild: disnake.Guild) -> None:
    """Log when the bot has joined a guild."""
    logger.info("Shoresy has joined %s (%s)", str(guild), str(guild.id))


@plugin.listener()
async def on_guild_remove(guild: disnake.Guild) -> None:
    """Log when the bot has left a guild."""
    await plugin.bot.remove_guild_members(guild.id)
    logger.info("Shoresy has left %s (%s)", str(guild), str(guild.id))


@plugin.listener()
async def on_member_remove(member: disnake.Member) -> None:
    '''Member left the guild.'''
    await plugin.bot.remove_member(member, all_guilds=False)
    logger.info('%s left %s and was removed from the database', str(member), str(member.guild))


setup, teardown = plugin.create_extension_handlers()
