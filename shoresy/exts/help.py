import disnake
from disnake.ext import plugins as p

from shoresy import log
from shoresy.bot import Shoresy

plugin = p.Plugin[Shoresy]()

logger = log.get_logger(__name__)


@plugin.slash_command(name="help")
async def help_command(inter: disnake.GuildCommandInteraction) -> None:
    """Display info, commands, and privacy terms."""
    remove = plugin.bot.get_global_command_named("remove")

    if remove is None:
        logger.warning("Unable to find `remove` command - help command errored.")
        await inter.response.send_message(
            "There was an error with this command.  Please try again shortly.",
            ephemeral=True,
        )
        return

    embed = disnake.Embed(
        title=f"{plugin.bot.user.name} help",
        description="Over 70 of your favorite chirps and quotes from all seasons of Letterkenny and Shoresy",
    )
    embed.set_thumbnail(
        url=plugin.bot.user.avatar.url if plugin.bot.user.avatar else None,
    )
    embed.add_field(
        name="Trigger Phrases:",
        value='"Fuck you, Shoresy"\n"it\'s fucking embarrassing"\n"How are ya now"\n"To be fair"\nothers...',
        inline=False,
    )
    embed.add_field(
        name="Commands:",
        value=f"</{remove.name}:{remove.id}> - Remove your stored member ID from the database (This means it will not be randomly drawn for certain responses)",
        inline=False,
    )
    embed.add_field(
        name="Privacy and Data Usage:",
        value="Using any of the trigger words will add your Discord member ID to the local database along with the ID of this guild. "
        'This data is only used for randomly selecting a member to mention in place of "Reilly" or "Jonesy" in certain quotes. '
        f"This data is not used in any other way and you may remove it any time with the </{remove.name}:{remove.id}> command.",
        inline=False,
    )

    button = disnake.ui.Button(
        label="Help/Docs",
        url="https://docs.dlchamp.com/en/letterkenny-bot",
    )
    await inter.response.send_message(embed=embed, components=[button])


setup, teardown = plugin.create_extension_handlers()
