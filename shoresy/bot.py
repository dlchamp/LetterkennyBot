import os
from datetime import datetime
from sys import version as sys_version
from typing import AsyncGenerator, ClassVar

import disnake
from disnake import __version__ as disnake_version
from disnake.ext import commands
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from shoresy import __version__ as bot_version

__all__ = ("Shoresy",)


class Shoresy(commands.InteractionBot):
    """Base bot instance"""

    db: ClassVar[AsyncGenerator[AsyncSession, None]]
    start_time: ClassVar[datetime]

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.images: dict[str, disnake.File] = {}
        self.quote_responses: list[str] = []
        self.fight_responses: list[str] = []

    async def on_ready(self) -> None:
        print(
            "----------------------------------------------------------------------\n"
            f'Bot started at: {datetime.now().strftime("%m/%d/%Y - %H:%M:%S")}\n'
            f"System Version: {sys_version}\n"
            f"Disnake Version: {disnake_version}\n"
            f"Bot Version: {bot_version}\n"
            f"Connected to Discord as {self.user} ({self.user.id})\n"
            "----------------------------------------------------------------------\n"
        )
        return

    async def load_extensions(self) -> None:
        """Load all extensions available on 'cogs'"""
        for item in os.listdir("shoresy/cogs"):

            name, ext = os.path.splitext(item)
            if "__" in name or ext != ".py":
                continue

            ext = f"shoresy.cogs.{name}"
            self.load_extension(ext)
            logger.info(f"Cog loaded: {ext}")

    def load_fight_responses(self) -> list[str]:
        """Loads the available fight responses from  the txt file"""

        with open("shoresy/core/responses/fight.txt") as f:
            self.fight_responses = f.readlines()

        logger.info(f"{len(self.fight_responses)} fight responses have been loaded")
        return self.fight_responses

    def load_shoresy_quotes(self) -> list[str]:
        """Loads all shoresy quotes from the txt file"""

        with open("shoresy/core/responses/shoresy.txt") as f:
            self.quote_responses = f.readlines()

        logger.info(f"{len(self.quote_responses)} quotes have been loaded")
        return self.quote_responses

    def load_image_responses(self) -> None:
        """Loads the images as `disnake.File` and store in `self.images`
        where image file name is the key"""

        path = "shoresy/core/images"

        for image in os.listdir(path):
            name, ext = os.path.splitext(image)

            if ext not in (".gif", ".jpg", ".png"):
                continue

            self.images[name] = disnake.File(f"{path}/{image}", filename=image)

        logger.info(f"{len(self.images)} images have been loaded.")

        return

    def check_response_cache(self) -> None:
        """Checks if the response and images cache is populated, else populates them"""
        if any(len(item) == 0 for item in [self.quote_responses, self.fight_responses]):
            self.load_bot_responses()

        if len(self.images) == 0:
            self.load_image_responses()
