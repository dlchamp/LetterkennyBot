from data import query
from disnake import ApplicationCommandInteraction, Message
from disnake.ext.commands import Cog, slash_command
from letterkennybot.modules.shoresy import response


class Shoresy(Cog):
    """Represents the message events that trigger from hot phrases"""

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self) -> None:
        """Invoked when this cog is loaded"""
        print(f"Cog loaded: {self.qualified_name}")

    @Cog.listener()
    async def on_message(self, message: Message) -> None:
        """Discord message event listener.  Only activated from trigger words"""

        if message.author.bot:
            return

        content = message.content.lower()
        member = message.author
        guild = message.guild

        # generate a response and send it to the channel
        reply = await response.get_response(
            content, member_id=member.id, guild_id=guild.id
        )
        if reply:
            # add the trigger author into the db if they do not already exist
            await query.add_member(member.id, guild.id)
            return await message.channel.send(reply)

    @slash_command(name="remove")
    async def remove_member(
        self, interaction: ApplicationCommandInteraction, _all: bool = False
    ) -> None:
        """Remove your member ID from the database

        Parameters
        ----------
        _all: (Default False) Remove your ID from database for all associated guilds"""
        try:
            await query.remove_member(
                interaction.author.id, interaction.guild.id, all_guilds=_all
            )
        except Exception as e:
            await interaction.response.send_message(
                "There was an error. It has been logged, please try again later",
                ephemeral=True,
            )

        else:
            if all:
                return await interaction.response.send_message(
                    "Your member ID was removed from the database", ephemeral=True
                )
            await interaction.response.send_message(
                f"Your member ID was removed from the database for {interaction.guild.name}",
                ephemeral=True,
            )
