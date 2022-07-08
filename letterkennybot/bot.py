"""
Handles the main bot constructor, load the bot modules and print
the ready message
"""
from sys import version as py_version

from disnake import Activity, ActivityType, Intents
from disnake import __version__ as disnake_version
from disnake.ext.commands import InteractionBot

from letterkennybot import __version__ as bot_version
from letterkennybot.modules.guild import GuildEvent
from letterkennybot.modules.help import Help
from letterkennybot.modules.shoresy import Shoresy

intents = Intents.default()
intents.message_content = True

bot = InteractionBot(
    intents=intents, activity=Activity(type=ActivityType.listening, name="/help")
)


@bot.listen("on_ready")
async def bot_ready():
    print(
        "------------------------------\n"
        f"{bot.user} has successfully connected to Discord\n"
        f"Python Version: {py_version}\n"
        f"Disnake Version: {disnake_version}\n"
        f"Bot Version: {bot_version}\n"
        "------------------------------"
    )


bot.add_cog(Shoresy(bot))
bot.add_cog(GuildEvent(bot))
bot.add_cog(Help(bot))
