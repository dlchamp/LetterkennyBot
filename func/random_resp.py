import random
import func.cache as db


def get_shoresy_quote(mention, guild_id, member_id):
    db.update_members_list(guild_id, member_id)
    with open("./quotes/quotes.txt") as file:
        quotes = file.read()
    quotes = list(map(str, quotes.split("\n")))
    ran_quotes = random.choices(quotes, k=4)
    quote = random.choice(ran_quotes)

    if 'Reilly' in quote or 'Jonesy' in quote:
        member = db.get_random_member(guild_id, member_id)
        if member is not None:
            return quote.replace('Reilly', member).replace('Jonesy', member).replace('{mention}', mention)

    return quote.replace('{mention}', mention)


def get_fight_words(guild_id, member_id):
    db.update_members_list(guild_id, member_id)
    with open("./quotes/fight.txt") as file:
        fight_words = file.read()

    fight_words = list(map(str, fight_words.split("\n")))
    return random.choice(fight_words)
