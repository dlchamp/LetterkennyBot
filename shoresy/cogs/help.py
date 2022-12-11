import disnake
from disnake.ext import commands

from shoresy.bot import Shoresy


class Help(commands.Cog):
    """Class that represents help related command and events"""

    def __init__(self, bot: Shoresy) -> None:
        self.bot = bot

    @commands.slash_command(name="help")
    async def help_command(self, interaction: disnake.GuildCommandInteraction):
        """Display info, commands, and privacy terms"""

        remove = self.bot.get_global_command_named("remove")

        embed = disnake.Embed(
            title=f"{self.bot.user.name} help",
            description="Over 70 of your favorite chirps and quotes from all seasons of Letterkenny and Shoresy",
        )
        embed.set_thumbnail(
            url=self.bot.user.avatar.url if self.bot.user.avatar else disnake.Embed.Empty
        )
        embed.add_field(
            name="Trigger Phrases:",
            value='"Fuck you, Shoresy"\n"it\'s fucking embarrassing"\n"How are ya now"\n"To be fair"\nothers...',
            inline=False,
        )
        embed.add_field(
            name="Commands:",
            value=f"</{remove.name}:{remove.id}> [all] - Remove your stored member ID from the database (This means it will not be randomly drawn for certain responses)",
            inline=False,
        )
        embed.add_field(
            name="Private and Data Usage:",
            value="Using any of the trigger words will add your Discord member ID to the local database along with the ID of this guild. "
            'This data is only used for randomly selecting a member to mention in place of "Reilly" or "Jonesy" in certain quotes. '
            f"This data is not used in any other way and you may remove it any time with the </{remove.name}:{remove.id}> command.",
            inline=False,
        )

        button = disnake.ui.Button(
            label="Help/Docs", url="https://docs.dlchamp.com/en/letterkenny-bot"
        )

        await interaction.response.send_message(embed=embed, components=[button])


def setup(bot: Shoresy) -> None:
    bot.add_cog(Help(bot))
