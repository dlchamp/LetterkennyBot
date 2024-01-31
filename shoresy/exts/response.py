import disnake
from disnake.ext import plugins as p

from shoresy import constants
from shoresy.bot import Shoresy

plugin = p.Plugin[Shoresy]()


@plugin.listener("on_message")
async def handle_message(message: disnake.Message) -> None:
    """Handle message triggers."""
    if message.author.bot or isinstance(message.author, disnake.User):
        return

    content_lower = message.content.lower()

    if any(word in content_lower for word in constants.SHORESY_TRIGGER):
        await plugin.bot.ensure_member(message.author)
        response = await plugin.bot.get_shoresy_response(message.author)
        await message.channel.send(response)

    elif "fucking embarrassing" in content_lower:
        image = disnake.File("shoresy/images/embarrassing.gif")
        await message.channel.send(file=image)

    elif any(phrase in content_lower for phrase in constants.HOW_ARE_YA_TRIGGER):
        await message.channel.send("Good'n you?", reference=message)

    elif "to be fair" in content_lower:
        image = disnake.File("shoresy/images/to_be_fair.gif")
        await message.channel.send(file=image)

    elif "toughest guy" in content_lower:
        image = disnake.File("shoresy/images/end_of_the_laneway.jpg")
        await message.channel.send(file=image, reference=message)

    elif "appreciates" in content_lower:
        await message.channel.send(
            f"Take about 10 to 15% off'er there, {message.author.mention}",
            reference=message,
        )

    elif any(phrase in content_lower for phrase in constants.GOOD_IDEA):
        await message.channel.send(
            "It's the best fuckin' idea I've ever heard in my life.",
            reference=message,
        )

    elif any(phrase in content_lower for phrase in constants.FIGHT_TRIGGER):
        response = plugin.bot.get_random_fight_response()
        await message.channel.send(response, reference=message)


setup, teardown = plugin.create_extension_handlers()
