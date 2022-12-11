import disnake
from disnake.ext import commands

from shoresy.bot import Shoresy
from shoresy.core.database import query


class Remove(commands.Cog):
    def __init__(self, bot: Shoresy) -> None:
        self.bot = bot

    @commands.slash_command(name="remove")
    async def remove_member(
        self,
        interaction: disnake.GuildCommandInteraction,
    ) -> None:
        """Remove your member ID from the database"""
        try:
            await query.remove_member(self.bot.db, member_id=interaction.author.id)
        except Exception as e:
            await interaction.response.send_message(
                "There was an error. It has been logged, please try again later",
                ephemeral=True,
            )
            raise

        else:

            message = f"Your member ID was removed from the database for {interaction.guild.name}"

            if all:
                message = "Your member ID was removed from the database"

            await interaction.response.send_message(message, ephemeral=True)


def setup(bot: Shoresy) -> None:
    bot.add_cog(Remove(bot))
