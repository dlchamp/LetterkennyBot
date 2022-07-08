from disnake import Guild
from disnake.ext.commands import Cog, InteractionBot


class GuildEvent(Cog):
    """Class that represents the guild join and leave events"""

    def __init__(self, bot):
        self.bot: InteractionBot = bot

    @Cog.listener(name="on_ready")
    async def guild_event_ready(self) -> None:
        print(f"Cog loaded: {self.qualified_name}")

    @Cog.listener()
    async def on_guild_join(self, guild: Guild) -> None:
        print(
            f"Bot has connected to {guild.name} ({guild.id}) | Members: {len(guild.members)}"
        )
        print(f"Now connected to {len(self.bot.guilds)}")

    @Cog.listener()
    async def on_guild_remove(self, guild: Guild) -> None:
        print(f"Bot has left {guild.name}")
        print(f"Now connected to {len(self.bot.guilds)}")
