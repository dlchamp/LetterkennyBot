import asyncio
import os
import signal
import sys

import disnake
from loguru import logger

from shoresy import constants
from shoresy.bot import Shoresy
from shoresy.core import database

_intents = disnake.Intents.none()
_intents.guilds = True
_intents.message_content = True
_intents.messages = True


async def main() -> None:
    """Create and run the bot"""

    bot = Shoresy(intents=_intents, reload=True if os.name == "nt" else False)
    bot.db = database.SessionLocal
    bot.start_time = disnake.utils.utcnow()

    try:
        await bot.load_extensions()
        bot.load_fight_responses()
        bot.load_shoresy_quotes()
        bot.load_image_responses()
    except Exception:
        await bot.close()
        raise

    logger.info("Bot is starting...")

    if os.name != "nt":
        # start process for linux based OS (Docker)

        loop = asyncio.get_event_loop()

        future = asyncio.ensure_future(bot.start(constants.Config.token or ""), loop=loop)
        loop.add_signal_handler(signal.SIGINT, lambda: future.cancel())
        loop.add_signal_handler(signal.SIGTERM, lambda: future.cancel())

        try:
            await future
        except asyncio.CancelledError:

            logger.warning("Kill command was sent to the bot. Closing bot and event loop")
            if not bot.is_closed():
                await bot.close()
    else:
        await bot.start(constants.Config.token)


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
