## Load env file ##
from dotenv import load_dotenv
load_dotenv()

## required import##
import os
import discord
import random
import time
import logging

logging.basicConfig(level = logging.INFO)
cooldown = True

## Comment this section out for non-Docker install ##
token = os.environ['TOKEN']

# If not using Docker, uncomment and replace BOT TOKEN with your token from Discord Developer ##
#token = ''

## open quotes.txt ##
with open("quotes/quotes.txt") as file:
	quotes = file.read()
	quote = list(map(str, quotes.split("\n")))

## open fights.txt ##
with open("quotes/fight.txt") as file:
	fights = file.read()
	fight = list(map(str, fights.split("\n")))

## open usernames list ##
with open("userlist/usernames.txt") as file:
	usernames = file.read()
	username = list(map(str, usernames.split("\n")))




## identify bot client ##
client = discord.Client()

fight_words = ["what's gunna happen?", "what's going to happen?","whats gunna happen?","whats going to happen?"
"what's gunna happen", "what's going to happen","whats gunna happen","whats going to happen","what's gonna happen",
"what's gonna happen","whats gonna happen","what is gonna happen","what is going to happen","what is gunna happen","what's gunna happen"]


## Set bot status
activity = discord.Activity(type=discord.ActivityType.watching, name="Letterkenny S10")


## log bot login event ##
@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity = activity)
	print("--------------------")
	print("Logged in as {0.user}.".format(client))
	print("Connected to servers:")
	print(client.guilds)
	print("--------------------")


## set bot icon ##
#@client.event
#async def on_ready():
#	await client.user.edit(avatar=icon)

## begin discord message and response events ##
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	msg = message.content
	
## Responds with random Shoresy quote - quotes found in quotes/quotes.txt ##
	## Prints message, author, channel, and server info to console
	## Prints response output to console

	if "shoresy" in msg.lower():
		mentioned = message.author.mention
		quote_reply = random.choice(quote)
		random_mention = random.choice(username)
		random_reply = quote_reply.replace("{mention}", mentioned).replace("{random}", random_mention)
		await message.channel.send(random_reply)
		print(f"{message.author} | {message.channel} | {message.guild.name} - `{msg}`")
		print(f"Replied with: '{random_reply}")




## Responds with embarrassing.gif ##
	## Prints message, author, channel, and server info to console
	## Prints response output to console

	if "fucking embarrassing" in msg.lower():
		await message.channel.send(file=discord.File('img/embarrassing.gif'))
		print(f"{message.author} | {message.channel}| {message.guild.name} - '{msg}'")
		print("emarrassing.gif sent to the channel")



## Responds with random Shoresy fight comeback - quotes found in quotes/fight.txt##
	## Prints message, author, channel, and server info to console
	## Prints response output to console

	if any(word in msg.lower() for word in fight_words):
		random_fight = random.choice(fight)
		await message.channel.send(random_fight)
		print("{message.author} | {message.channel}| {message.guild.name} - '{msg}'")
		print("Responding with '{random_fight}'")



## Responds with "'Good'n You"##
## Prints message, author, channel, and server info to console
## Prints response output to console

	if "how are ya now" in msg.lower():
		await message.channel.send("Good'n you?")
		print(f"{message.author} | {message.channel}| {message.guild.name} - '{msg}'")
		print("Responding with 'Good'n you?'")



## Responds with to_be_fair.gif##
	## Prints message, author, channel, and server info to console
	## Prints response output to console

	if "to be fair" in msg.lower():
		await message.channel.send(file=discord.File('img/to_be_fair.gif'))
		print(f"{message.author} | {message.channel}| {message.guild.name} - '{msg}'")
		print("to_be_fair.gif sent to the channel")



## Responds with end_of_the_laneway.jpg##
	## Prints message, author, channel, and server info to console
	## Prints response output to console

	if "toughest guy" in msg.lower():
		await message.channel.send(file=discord.File('img/end_of_the_laneway.jpg'))
		print(f"{message.author} | {message.channel}| {message.guild.name} - '{msg}'")
		print("end_of_the_laneway.jpg sent to the channel")



## Responds with birthday.gif##
## Prints message, author, channel, and server info to console
## Prints response output to console

	global cooldown
	if "happy birthday" in msg.lower() and cooldown:
		cooldown = False
		await message.channel.send("https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/birthday.gif")
		print(f"{message.author} | {message.channel} | {message.guild.name} - '{msg}'")
		print("birthday.gif sent to channel")
		time.sleep(600)
		cooldown = True





client.run(token)