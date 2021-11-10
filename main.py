import os
import random
import datetime
import logging
import time
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv


'''
Quotes sections - open quote files
'''
# 40+ quotes from Shoresy, Wayne, and other characters
with open("quotes/quotes.txt") as file:
    quotes = file.read()
    quote = list(map(str, quotes.split("\n")))

# Responses to "What's going to happen?"
with open("quotes/fight.txt") as file:
    fights = file.read()
    fight = list(map(str, fights.split("\n")))

'''
Variations of trigger phrases
'''
fight_words = ["what's gunna happen", "whats gunna happen", "what's gonna happen",
               "whats gonna happen", "what's going to happen", "whats going to happen"]

shoresy = ['fuck you shoresy', 'fuck you, shoresy']


'''
Setup bot and configure status
'''
bot = commands.Bot(command_prefix="-", help_command=None,
                   case_insensitive=True)

activity = nextcord.Activity(
    type=nextcord.ActivityType.watching, name="-help")

'''
Start Discord event functions.
'''

# On Ready event - When bot has connected to Discord and has become ready, print:
# Bot name, bot ID, and guilds that bot is currecntly connected to.


@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.online, activity=activity)
    print('--------------------')
    print(
        f'Bot is online and ready!\nConnected as {bot.user.name} ({bot.user.id})')
    print(f'Connected to {len(bot.guilds)} guild(s)')
    for guild in bot.guilds:
        print(f'{guild.name} ({guild.id})')
    print('--------------------')


@bot.event
async def on_guild_join(guild):
    print(f'Bot has connected to {guild.name}')


@bot.event
async def on_guild_remove(guild):
    print(f'Bot has left {guild.name}')


'''
Invite command - Sends the command user a DM with an invite link for this bot.
'''


@ bot.command(name='invite')
async def invite(ctx,):

    user = await bot.fetch_user(ctx.author.id)
    try:
        await ctx.send(f'Check your DMs, {ctx.author.mention}')
        await user.send("Invite me to your server with this link.\nhttps://discord.com/api/oauth2/authorize?client_id=873640710480486451&permissions=117760&scope=bot")
    except:
        await ctx.send(f"Tried to DM you the invite link, {ctx.author.mention}\nAttaching it here instead.\nhttps://discord.com/api/oauth2/authorize?client_id=873640710480486451&permissions=117760&scope=bot")


# Sets on_message cooldown to 10 minutes (600 seconds) for the channel, only in use for 'Happy birhtday' message
cd = commands.CooldownMapping.from_cooldown(
    1, 600.0, commands.BucketType.channel)


def get_ratelimit(message):
    bucket = cd.get_bucket(message)
    return bucket.update_rate_limit()


@ bot.event
async def on_message(message):
    ratelimit = get_ratelimit(message)
    mentioned = message.author.mention
    msg = message.content
    if message.author == bot.user:
        return

    if any(word in msg.lower() for word in shoresy):
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

    if "what i appreciates" in msg.lower():
        await message.channel.send(f'Take about 10 to 15% off\'er there, {mentioned}')

    # Required to allow bot to process commands
    await bot.process_commands(message)

load_dotenv()
bot.run(os.environ['TOKEN'])
