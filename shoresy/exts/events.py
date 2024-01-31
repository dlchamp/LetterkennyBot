import disnake
from disnake.ext import plugins as p

from shoresy import log
from shoresy.bot import Shoresy

plugin = p.Plugin[Shoresy]()
logger = log.get_logger(__name__)


@plugin.listener()
async def on_guild_join(guild: disnake.Guild) -> None:
    """Log when the bot has joined a guild."""
    logger.info(f"Shoresy has joined {guild} ({guild.id})")


@plugin.listener()
async def on_guild_remove(guild: disnake.Guild) -> None:
    """Log when the bot has left a guild."""
    logger.info(f"Shoresy has left {guild} ({guild.id})")


setup, teardown = plugin.create_extension_handlers()
