from disnake import ApplicationCommandInteraction, Embed
from disnake.ext.commands import Cog, slash_command


class Help(Cog):
    """Class that represents help related command and events"""

    def __init__(self, bot) -> None:
        self.bot: InteractionBot = bot

    @Cog.listener()
    async def on_ready(self) -> None:
        """Invoked when this cog is loaded"""
        print(f"Cog loaded: {self.qualified_name}")

    @slash_command(name="help")
    async def help_command(self, interaction: ApplicationCommandInteraction):
        """Display info, commands, and privacy terms"""

        embed = Embed(
            title=f"{self.bot.user.name} help",
            description="Over 60 of your favorite chirps and quotes from seasons 1-10 of Letterkenny and season 1 of Shoresy",
        )
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.add_field(
            name="Trigger Phrases:",
            value='"Fuck you, Shoresy"\n"it\'s fucking embarrassing"\n"How are ya now"\n"To be fair"\nothers...',
            inline=False,
        )
        embed.add_field(
            name="Commands:",
            value="`/remove` - Remove your stored member ID from the database",
            inline=False,
        )
        embed.add_field(
            name="Private and Data Usage:",
            value="Using any of the trigger words will add your Discord member ID to the local database along with the ID of this guild. "
            'This data is only used for randomly selecting a member to mention in place of "Reilly" or "Jonesy" in certain quotes. '
            "This data is not used in any other way and you may remove it any time with the `/remove` command.",
            inline=False,
        )

        await interaction.response.send_message(embed=embed)
