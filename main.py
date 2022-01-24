import os
import random

import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv

import func.cache as db
import func.random_resp as rand


'''
Trigger phrases/words
'''
fight_words = ["what's gunna happen", "whats gunna happen", "what's gonna happen",
               "whats gonna happen", "what's going to happen", "whats going to happen"]
shoresy = ['fuck you shoresy', 'fuck you, shoresy']
shoresy_wrong = ['fuck you shorsey', 'fuck you, shorsey']
how_are_ya = ['how\'re ya now', 'how are ya now', 'how\'r ya now']


'''
Setup bot and configure status
'''
bot = commands.Bot(command_prefix="-", help_command=None,
                   case_insensitive=True)
activity = nextcord.Activity(
    type=nextcord.ActivityType.watching, name="Letterkenny S10")


@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.online, activity=activity)
    print('--------------------')
    print(
        f'Bot is online and ready!')
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


@bot.command(name='remove')
async def remove_member(ctx):
    guild_id = str(ctx.guild.id)
    member_id = f'<@{ctx.author.id}>'
    remove = db.remove_member(guild_id, member_id)
    if remove:
        await ctx.message.reply('You were removed from the DB. You will no longer be tagged in Shoresy quotes')
    elif not remove:
        await ctx.message.reply('Seems your discord ID hasn\'t been stored - Nothing to remove.')
    else:
        await ctx.send('There was an error. Please try again later.')


@bot.command(name='help')
async def help_command(ctx):
    embed = nextcord.Embed(title='LetterkennyBot Help',
                           description=f'{bot.user.name} brings you over 50 of your favorite chips from gang. These tips should help get you and your friends on the way to getting roasted.')
    embed.add_field(name='Hotwords/Phrase', value='"Fuck you, Shoresy"\n"Fucking embarrassing"\n \
        "How are ya now"\n"To be fair"\n"Toughest guy"\n"Happy Birthday" (*10 minute usage cooldown*)\n"what I appreciates"', inline=False)
    embed.add_field(
        name='Commands', value=f'`{ctx.prefix}remove` - Removes your Discord ID from the database.', inline=False)
    embed.add_field(name='Data usage information:',
                    value=f'Using the "Fuck you, Shoresy" hot phrase will add your Discord ID to a database. \
                    This database is only used to randomly select a member to replace "Reilly" or "Jonesy" in quotes. \
                    You can delete your ID from this list at anytime with `{ctx.prefix}remove`\n \
                    (*Example: "Fuck you, `@Reilly`. Your mum sneaky gushed so hard she bucked me off the waterbed last night. Don\'t tell her I was thinking about `@Jonesy\'s` mum the entire time."*)', inline=False)
    await ctx.send(embed=embed)


# Sets on_message cooldown to 10 minutes (600 seconds) for the channel, only in use for 'Happy birhtday' message
cd = commands.CooldownMapping.from_cooldown(
    1, 600.0, commands.BucketType.channel)


def get_ratelimit(message):
    bucket = cd.get_bucket(message)
    return bucket.update_rate_limit()


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    ratelimit = get_ratelimit(message)
    msg = message.content
    mention = member_id = f'<@{message.author.id}>'
    guild_id = str(message.guild.id)

    if any(word in msg.lower() for word in shoresy):
        reply = rand.get_shoresy_quote(mention, guild_id, member_id)
        await message.channel.send(reply)

    if any(word in msg.lower() for word in shoresy_wrong):
        reply = f'Fuck you, {mention}. You can\'t even spell my name right. Give yer balls a tug.'
        await message.channel.send(reply)

    if "fucking embarrassing" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/embarrassing.gif")

    if any(word in msg.lower() for word in fight_words):
        reply = rand.get_fight_words(guild_id, member_id)
        await message.channel.send(reply)

    if any(word in msg.lower() for word in how_are_ya):
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
