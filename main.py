## Load env file ##
from dotenv import load_dotenv
load_dotenv()

## required import##
import os
import discord
import random

## Comment this section out for non-Docker install ##
token = os.environ['TOKEN']

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

## open usernames list ##
with open("userlist/usernames.txt") as file:
	usernames = file.read()
	username = list(map(str, usernames.split("\n")))




## identify bot client ##
client = discord.Client()

fight_words = ["what's gunna happen?", "what's going to happen?","whats gunna happen?","whats going to happen?"
"what's gunna happen", "what's going to happen","whats gunna happen","whats going to happen","what's gonna happen",
"what's gonna happen","whats gonna happen","what is gonna happen","what is going to happen","what is gunna happen","what's gunna happen"]


## log bot login event ##
@client.event
async def on_ready():
	print('We have logged in as {0.user}'
		.format(client))

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
	
		
	if "shoresy" in msg.lower():
		mentioned = message.author.mention
		quote_reply = random.choice(quote)
		random_mention = random.choice(username)
		random_reply = quote_reply.replace("{mention}", mentioned).replace("{random}", random_mention)
		
#		print(random_reply)
		await message.channel.send(random_reply)

	if "fucking embarrassing" in msg.lower():
		await message.channel.send(file=discord.File('img/embarrassing.gif'))

	if any(word in msg.lower() for word in fight_words):
		await message.channel.send(random.choice(fight))

	if "how are ya now" in msg.lower():
		await message.channel.send("Good'n you?")

	if "to be fair" in msg.lower():
		await message.channel.send(file=discord.File('img/to_be_fair.gif'))

	if "birthday" in msg.lower():
		await message.channel.send(file=discord.File('img/birthday.gif'))


client.run(token)