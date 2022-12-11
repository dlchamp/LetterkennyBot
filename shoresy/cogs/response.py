import random

import disnake
from disnake.ext import commands

from shoresy.bot import Shoresy
from shoresy.core.database import query

FIGHT_TRIGGERS: list = [
    "what's gunna happen",
    "whats gunna happen",
    "what's gonna happen",
    "whats gonna happen",
    "what's going to happen",
    "whats going to happen",
]
SHORESY_TRIGGERS: list = ["fuck", "you", "shoresy"]

HOW_ARE_YA_TRIGGERS: list = [
    "how're ya now",
    "how are ya now",
    "how'r ya now, howr ya now",
]


class Response(commands.Cog):
    def __init__(self, bot: Shoresy) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message) -> None:
        """Discord message event"""

        if message.author.bot:
            return

        content = message.content.lower()
        member = message.author
        guild = message.guild

        reply = await self.get_response(content, member.id, guild.id)
        if reply:
            if isinstance(reply, disnake.File):
                await message.channel.send(file=reply)

            else:
                await message.channel.send(reply)

            await query.add_member(self.bot.db, member_id=member.id, guild_id=guild.id)

    async def get_response(self, content: str, member_id: int, guild_id: int) -> str | disnake.File:
        """Generates a response based on the trigger word and returns the response"""

        if all(word in content for word in SHORESY_TRIGGERS):
            return await self.shoresy_response(member_id, guild_id)

        if "fucking embarrassing" in content:
            return self.bot.images.get("embarrassing")

        if any(phrase in content for phrase in FIGHT_TRIGGERS):
            return self.fight_response()

        if any(phrase in content for phrase in HOW_ARE_YA_TRIGGERS):
            return "Good'n you?"

        if "to be fair" in content:
            return self.bot.images.get("to_be_fair")

        if "toughest guy" in content:
            return self.bot.images.get("end_of_the_laneway")

        if "appreciates" in content:
            return f"Take about 10 to 15% off'er there, <@{member_id}>"

        if any(word in content for word in ["great idea", "good idea"]):
            return "It's the best fuckin' idea I've ever heard in my life."

    async def shoresy_response(self, member_id: int, guild_id: int) -> str:
        """Generates a response for the "fuck you shoresy" trigger phrase"""

        responses = self.bot.quote_responses
        # reload quotes if all have been used
        if not responses:
            responses = self.bot.load_shoresy_quotes()

        # check length of available responses
        k = len(responses) if len(responses) < 5 else 5

        selection = random.choices(responses, k=k)
        selected = random.choice(selection)
        self.bot.quote_responses.remove(selected)

        second_member = await query.get_random_member(
            self.bot.db, member_id=member_id, guild_id=guild_id
        )

        if second_member is None and "{second}" in selected:
            return await self.shoresy_response(member_id, guild_id)

        return selected.replace("{second}", f"<@{second_member}>").replace(
            "{mention}", f"<@{member_id}>"
        )

    def fight_response(self) -> str:
        """Generate a response for the 'what's gunna happen' trigger phrase"""
        responses = self.bot.fight_responses
        if not responses:
            responses = self.bot.load_fight_responses()

        response = random.choice(responses)
        self.bot.fight_responses.remove(response)

        return response


def setup(bot: Shoresy) -> None:
    bot.add_cog(Response(bot))
