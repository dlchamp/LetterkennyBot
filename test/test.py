import random

## open and read from quotes.txt ##
with open("quotes.txt") as file:
	quotes = file.read()
	quote = list(map(str, quotes.split("\n")))

## open and ready from fight.txt ##
with open("fight.txt") as file:
	fights = file.read()
	fight = list(map(str, fights.split("\n")))

## open usernames list ##
with open("usernames.txt") as file:
	usernames = file.read()
	username = list(map(str, usernames.split("\n")))

## open usernames list ##
with open("mention.txt") as file:
	mentions = file.read()
	mention = list(map(str, mentions.split("\n")))


quote_response = random.choice(quote)
mentioned = random.choice(mention)
random_user = random.choice(username)
message = quote_response.replace('{mention}',mentioned).replace('{random}', random_user)



print(message)
print()
