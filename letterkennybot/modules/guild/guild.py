import disnake
from disnake.ext import commands


class GuildEvent(commands.Cog):
    """Class that represents the guild join and leave events"""

    def __init__(self, bot: commands.InteractionBot):
        self.bot = bot

    @commands.Cog.listener(name="on_ready")
    async def guild_event_ready(self) -> None:
        print(f"Cog loaded: {self.qualified_name}")

    @commands.Cog.listener()
    async def on_guild_join(self, guild: disnake.Guild) -> None:
        print(
            f"Bot has connected to {guild.name} ({guild.id}) | Members: {len(guild.members)}"
        )
        print(f"Now connected to {len(self.bot.guilds)}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: disnake.Guild) -> None:
        print(f"Bot has left {guild.name}")
        print(f"Now connected to {len(self.bot.guilds)}")
