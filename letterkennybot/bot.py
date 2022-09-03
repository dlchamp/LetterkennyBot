"""
Handles the main bot constructor, load the bot modules and print
the ready message

-----------------------------------------------------------------

MIT License

Copyright (c) 2022 DLCHAMP

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from sys import version as py_version

import disnake
from disnake import __version__ as disnake_version
from disnake.ext import commands

from letterkennybot import __version__ as bot_version
from letterkennybot.modules.guild import GuildEvent
from letterkennybot.modules.help import Help
from letterkennybot.modules.shoresy import Shoresy

intents = disnake.Intents.none()
intents.guild_messages = True
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.InteractionBot(
    intents=intents,
    activity=disnake.Activity(type=disnake.ActivityType.listening, name="/help"),
)


@bot.listen("on_ready")
async def bot_ready():
    print(
        "------------------------------\n"
        f"{bot.user} has successfully connected to Discord\n"
        f"Python Version: {py_version}\n"
        f"Disnake Version: {disnake_version}\n"
        f"Bot Version: {bot_version}\n"
        f"Connected to {len(bot.guilds)} guilds with  a total of {len(bot.users)} members\n"
        "------------------------------"
    )


bot.add_cog(Shoresy(bot))
bot.add_cog(GuildEvent(bot))
bot.add_cog(Help(bot))
