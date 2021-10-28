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
    type=discord.ActivityType.watching, name="-help")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('--------------------')
    print(f'Bot is online and ready!\nConnected as {bot.user.name} ({bot.user.id})')
    print(f'Connected to {len(bot.guilds)} guild(s)')
    for guild in bot.guilds:
        print(guild.name)
    print('--------------------')


# announce server join in console if bot is connected to a server after running


@bot.event
async def on_guild_join(guild):
    name = guild.name


# announce server leave in console if bot is removed from a server after running
@bot.event
async def on_guild_remove(guild):
    name = guild.name


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


## Message cooldown
cd = commands.CooldownMapping.from_cooldown(1,600.0, commands.BucketType.channel)
def get_ratelimit(message):
    bucket = cd.get_bucket(message)
    return bucket.update_rate_limit()

## begin discord message and response events ##
@bot.event
async def on_message(message):
    ratelimit = get_ratelimit(message)
    msg = message.content
    if message.author == bot.user:
        return

    if any(word in msg.lower() for word in shoresy):
        mentioned = message.author.mention
        reply_list = random.choices(quote, k=3)
        quote_reply = random.choice(reply_list)
        random_reply = quote_reply.replace("{mention}", mentioned)
        await message.channel.send(random_reply)

    if "fucking embarrassing" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/embarrassing.gif")

    if any(word in msg.lower() for word in fight_words):
        random_fight = random.choice(fight)
        await message.channel.send(random_fight)

    if "how are ya now" in msg.lower():
        await message.channel.send("Good'n you?")

    if "to be fair" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/to_be_fair.gif")


    if "toughest guy" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/end_of_the_laneway.jpg")

    if "happy birthday" in msg.lower():
        if ratelimit is None:
            await message.channel.send('https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/birthday.gif')

    await bot.process_commands(message)


bot.run(token)
