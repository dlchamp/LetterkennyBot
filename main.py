## Load env file ##
from dotenv import load_dotenv
load_dotenv()

## required import##
import os
import discord
from discord.ext import commands
import random
import time
import logging
import datetime
import time


logging.basicConfig(level=logging.WARNING)

## Comment this section out for non-Docker install ##
token = os.environ['TOKEN']


## identify bot bot ##
bot = commands.Bot(command_prefix="-", help_command=None,
                   case_insensitive=True)

# If not using Docker, uncomment and replace BOT TOKEN with your token from Discord Developer ##
#token = 'BOT TOKEN'

## open quotes.txt ##
with open("quotes/quotes.txt") as file:
    quotes = file.read()
    quote = list(map(str, quotes.split("\n")))

## open fights.txt ##
with open("quotes/fight.txt") as file:
    fights = file.read()
    fight = list(map(str, fights.split("\n")))


fight_words = ["what's gunna happen", "whats gunna happen", "what's gonna happen",
               "whats gonna happen", "what's going to happen", "whats going to happen"]

shoresy = ['fuck you shoresy', 'fuck you, shoresy']


# Set bot status
activity = discord.Activity(
    type=discord.ActivityType.watching, name="-help | Letterkenny S10")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("--------------------")
    print("Logged in as {0.user}.".format(bot))
    print("Connected to servers:")
    for name in bot.guilds:
        print(f"-- {name} --")
    print("--------------------")

# announce server join in console if bot is connected to a server after running


@bot.event
async def on_guild_join(guild):
    name = guild.name
    print(f"Joined new server: {name}")


# announce server leave in console if bot is removed from a server after running
@bot.event
async def on_guild_remove(guild):
    name = guild.name
    print(f"Removed from server: {name}")


# start bot commands

# Respond with Help embed
@bot.command()
async def help(ctx):
    time = datetime.datetime.utcnow()
    embed = discord.Embed(
        title='\u200b', description='`-help` to bring up this menu', timestamp=time)
    embed.set_author(name='LetterkennyBot',
                     icon_url='https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/container_icon.png')
    embed.add_field(
        name='Phrases', value='"Fuck you shoresy"\n"To be fair"\n"How are ya now"\n"What\'s gunna happen?"\n"Fucking embarrassing"\n"toughest guy in Letterkenny"')
    embed.add_field(name="General Commands",
                    value="`-invite` - DMs a link to add this bot to your server\n")
    embed.set_footer(
        text=f"Requested by: {ctx.author.name}", icon_url=bot.user.avatar_url)

    await ctx.send(embed=embed)


# invite link sent to command author DM
@bot.command(name='invite')
async def invite(ctx,):

    user = await bot.fetch_user(ctx.author.id)
    try:
        await ctx.send(f'Check your DMs, {ctx.author.mention}')
        await user.send("Invite me to your server with this link.\nhttps://discord.com/api/oauth2/authorize?client_id=873640710480486451&permissions=117760&scope=bot")
    except:
        await ctx.send(f"Tried to DM you the invite link, {ctx.author.mention}\nAttaching it here instead.\nhttps://discord.com/api/oauth2/authorize?client_id=873640710480486451&permissions=117760&scope=bot")


## begin discord message and response events ##
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content


## Responds with random Shoresy quote - quotes found in quotes/quotes.txt ##
    # Prints message, author, channel, and server info to console
    # Prints response output to console

    if any(word in msg.lower() for word in shoresy):
        mentioned = message.author.mention
        reply_list = random.choices(quote, k=3)
        quote_reply = random.choice(reply_list)
        random_reply = quote_reply.replace("{mention}", mentioned)
        await message.channel.send(random_reply)

        print(
            f"{message.author.name} | {message.channel} | {message.guild.name} - `{msg}`")
        print(f"Replied with: '{random_reply}")


## Responds with embarrassing.gif ##
    # Prints message, author, channel, and server info to console
    # Prints response output to console

    if "fucking embarrassing" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/embarrassing.gif")

        print(
            f"{message.author.name} | {message.channel}| {message.guild.name} - '{msg}'")
        print("emarrassing.gif sent to the channel")


## Responds with random Shoresy fight comeback - quotes found in quotes/fight.txt##
    # Prints message, author, channel, and server info to console
    # Prints response output to console

    if any(word in msg.lower() for word in fight_words):
        random_fight = random.choice(fight)
        await message.channel.send(random_fight)

        print(
            f"{message.author.name} | {message.channel}| {message.guild.name} - '{msg}'")
        print(f"Responding with '{random_fight}'")


## Responds with "'Good'n You"##
# Prints message, author, channel, and server info to console
# Prints response output to console

    if "how are ya now" in msg.lower():
        await message.channel.send("Good'n you?")

        print(
            f"{message.author.name} | {message.channel}| {message.guild.name} - '{msg}'")
        print("Responding with 'Good'n you?'")


## Responds with to_be_fair.gif##
    # Prints message, author, channel, and server info to console
    # Prints response output to console

    if "to be fair" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/to_be_fair.gif")

        print(
            f"{message.author.name} | {message.channel}| {message.guild.name} - '{msg}'")
        print("to_be_fair.gif sent to the channel")


## Responds with end_of_the_laneway.jpg##
    # Prints message, author, channel, and server info to console
    # Prints response output to console

    if "toughest guy" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/end_of_the_laneway.jpg")

        print(
            f"{message.author.name} | {message.channel}| {message.guild.name} - '{msg}'")
        print("end_of_the_laneway.jpg sent to the channel")

    if "happy birthday" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/birthday.gif")
        await asyncio.sleep(300)

    await bot.process_commands(message)


bot.run(token)
