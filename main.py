from disnake import (
    Activity,
    ActivityType,
    Status,
    Intents,
    Embed
    )
from disnake.ext import commands, tasks

from os import getenv
from dotenv import load_dotenv
from random import choice
from asyncio import sleep

# local imports
import func.cache as db
import func.random_resp as rand


'''
Trigger phrases/words
'''
fight_words = [
    "what's gunna happen", "whats gunna happen",
    "what's gonna happen", "whats gonna happen",
    "what's going to happen", "whats going to happen"
    ]

shoresy = [
    'fuck you shoresy', 'fuck you, shoresy'
    ]

shoresy_wrong = [
    'fuck you shorsey', 'fuck you, shorsey'
    ]

how_are_ya = [
    'how\'re ya now', 'how are ya now',
    'how\'r ya now'
    ]

shoresy_wrong_resp = [
    'Fuck you {mention}, can\'t even spell my name. Give yer balls a tug.',
    'Wish you weren\'t so fuckin\' akward, bud.',
    'Fuck, Lemony Snicket. What Series of Unfortunate Events you been through, you ugly fuck?'
    ]


# # list of activities
# statuses = [
#     "-help | Rewatching Letterkenny",
#     "-help | Chirpin' {guild_count} guilds.",
#     "-help | Crushing sandos",
#     "-help | Yahtzee",
#     "-help | Ref'ing girls hockey"
#     ]

# used_statuses = []


# instantiate the bot, declare intents, and set activity status
# Intents.members - only necessary for calculating activity for "serving guilds/chirping member #"
intents = Intents.default()
intents.members=True

bot = commands.Bot(
    command_prefix="-",
    help_command=None,
    case_insensitive=True,
    intents=intents
    )



@bot.listen()
async def on_ready():

    print()
    print(f'{bot.user} is alive and listening to Discord events')
    print('-'*30)
    print(f'Connected to: {len(bot.guilds)} guild(s)')
    print('\n'.join(
        [f'{guild.name} ({guild.id}) | Members: {len(guild.members)}' for guild in bot.guilds]
        ))
    print('-'*30)


@bot.listen()
async def on_guild_join(guild):
    print(f'Bot has connected to {guild.name} ({guild.id}) | Members: {len(guild.members)}')


@bot.listen()
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
    embed = Embed(
        title='LetterkennyBot Help',
        description=f'{bot.user.name} brings you over 50 of your favorite chips from gang. These tips should help get you and your friends on the way to getting roasted.')

    embed.add_field(
        name='Hotwords/Phrase',
        value='"Fuck you, Shoresy"\n"Fucking embarrassing"\n"How are ya now"\n"To be fair"\n"Toughest guy"\n"Happy Birthday" (*10 minute usage cooldown*)\n"what I appreciates"', inline=False)

    embed.add_field(
        name='Commands',
        value=f'`{ctx.prefix}remove` - Removes your Discord ID from the database.', inline=False)

    embed.add_field(
        name='Data usage information:',
        value=f'Using the "Fuck you, Shoresy" hot phrase will add your Discord ID to a database. This database is only used to randomly select a member to replace "Reilly" or "Jonesy" in quotes. You can delete your ID from this list at anytime with `{ctx.prefix}remove`\n(*Example: "Fuck you, `@Reilly`. Your mum sneaky gushed so hard she bucked me off the waterbed last night. Don\'t tell her I was thinking about `@Jonesy\'s` mum the entire time."*)', inline=False)

    await ctx.send(embed=embed)


# Sets on_message cooldown to 10 minutes (600 seconds) for the guild, only in use for 'Happy birhtday' message
cd = commands.CooldownMapping.from_cooldown(
    1, 600.0, commands.BucketType.guild)


def get_ratelimit(message):
    bucket = cd.get_bucket(message)
    return bucket.update_rate_limit()


@bot.listen()
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

    elif any(word in msg.lower() for word in shoresy_wrong):
        reply = choice(shoresy_wrong_resp).replace('{mention}', mention)
        await message.channel.send(reply)

    elif "fucking embarrassing" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/embarrassing.gif")

    elif any(word in msg.lower() for word in fight_words):
        reply = rand.get_fight_words(guild_id, member_id)
        await message.channel.send(reply)

    elif any(word in msg.lower() for word in how_are_ya):
        await message.channel.send("Good'n you?")

    elif "to be fair" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/to_be_fair.gif")

    elif "toughest guy" in msg.lower():
        await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/end_of_the_laneway.jpg")

    elif "happy birthday" in msg.lower():
        if ratelimit is None:
            await message.channel.send('https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/birthday.gif')

    elif "what i appreciates" in msg.lower():
        await message.channel.send(f'Take about 10 to 15% off\'er there, {mention}')



@tasks.loop(count=1)
async def update_status(bot):
    '''task loop that randomly updates bot status every minute'''

    # wait for bot internal cache is ready - only matters during first run
    await bot.wait_until_ready()

    activity = Activity(type=ActivityType.listening, name='-help')
    await bot.change_presence(status=Status.online, activity=activity)

    # get guild data
    # guild_count = str(len(bot.guilds))
    # mem_count = sum([len(guild.members) for guild in bot.guilds])


    # while True:
    #     ran_status = choice(statuses).replace('{guild_count}', guild_count)

    #     if len(statuses) == len(used_statuses):
    #         used_statuses.clear()

    #     if not ran_status in used_statuses:
    #         used_statuses.append(ran_status)

    #         #set the activity type and name
    #         activity = Activity(type=ActivityType.streaming, name=ran_status)

    #         # update the status
    #         await bot.change_presence(status=Status.online, activity=activity)
    #         print(f'Status updated: {ran_status}')

    #         break




if __name__ == '__main__':

    load_dotenv()
    update_status.start(bot)
    bot.run(getenv('TOKEN'))




