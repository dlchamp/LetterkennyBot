import asyncio
import os
import signal
import sys

import disnake

from shoresy import constants, log
from shoresy.bot import Shoresy

logger = log.get_logger(__name__)

_intents = disnake.Intents.none()
_intents.guilds = True
_intents.message_content = True
_intents.messages = True


async def main() -> None:
    """Create and run the bot."""
    bot = Shoresy(intents=_intents, reload=constants.DEV_MODE)
    bot.start_time = disnake.utils.utcnow()

    try:
        bot.load_extensions("shoresy/exts")

    except Exception:
        await bot.close()
        raise

    try:
        if os.name != "nt":
            # start process for linux host
            loop = asyncio.get_event_loop()

            future = asyncio.ensure_future(bot.start(constants.Config.token), loop=loop)
            loop.add_signal_handler(signal.SIGINT, lambda: future.cancel())
            loop.add_signal_handler(signal.SIGTERM, lambda: future.cancel())

            await future

        else:
            await bot.start(constants.Config.token)

    except (asyncio.CancelledError, KeyboardInterrupt):
        logger.warning("Kill command received. Bot is closed.")
        if not bot.is_closed():
            await bot.close()


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
