import disnake
from disnake.ext import plugins as p
from disnake.ext import tasks

from shoresy.bot import Shoresy

plugin = p.Plugin[Shoresy]()


@plugin.load_hook()
async def start_tasks() -> None:
    """Start the tasks on plugin load."""
    set_activity.start()


@plugin.unload_hook()
async def stop_tasks() -> None:
    """Stop the tasks on plugin unload."""
    set_activity.stop()


@tasks.loop(count=1)
async def set_activity() -> None:
    """Set activity after bot is ready."""
    await plugin.bot.wait_until_ready()

    activity = disnake.Activity(
        type=disnake.ActivityType.custom,
        name="custom",
        state=f"Chirping in {len(plugin.bot.guilds)} guilds!",
    )
    await plugin.bot.change_presence(activity=activity)


setup, teardown = plugin.create_extension_handlers()
