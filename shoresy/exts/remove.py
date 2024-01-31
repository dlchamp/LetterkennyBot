import disnake
from disnake.ext import commands
from disnake.ext import plugins as p

from shoresy.bot import Shoresy

plugin = p.Plugin[Shoresy]()


@plugin.slash_command(name="remove")
async def remove_member(
    inter: disnake.GuildCommandInteraction,
    *,
    all_guilds: bool = commands.Param(False, name="all-guilds"),  # noqa: FBT003
) -> None:
    """Remove yourself from the database - Prevents tags in certain Shoresy responses.

    Parameters
    ----------
    all-guilds: bool
        If False, your ID is only removed from the association from this guild.  (Default False)
    """
    msg = (
        "Your Discord user ID has been removed from the database "
        f"{'for ALL guilds' if all_guilds else f'for {inter.guild}'}."
    )

    await plugin.bot.remove_member(inter.author, all_guilds=all_guilds)
    await inter.response.send_message(msg, ephemeral=True)


setup, teardown = plugin.create_extension_handlers()
