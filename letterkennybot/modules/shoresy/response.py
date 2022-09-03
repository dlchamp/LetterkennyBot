"""
Generate response based on trigger word

---------------------------------------

MIT License

Copyright (c) 2022 DLCHAMP

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import random

from data import query

fight_triggers: list = [
    "what's gunna happen",
    "whats gunna happen",
    "what's gonna happen",
    "whats gonna happen",
    "what's going to happen",
    "whats going to happen",
]
shoresy_triggers: list = ["fuck", "you", "shoresy"]
how_are_ya_triggers: list = [
    "how're ya now",
    "how are ya now",
    "how'r ya now, howr ya now",
]


async def get_response(content: str, *, member_id: int, guild_id: int) -> str:
    """Generates a response based on the trigger word and returns the response"""

    if all(word in content for word in shoresy_triggers):
        return await shoresy_response(member_id, guild_id)

    if "fucking embarrassing" in content:
        return "https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/embarrassing.gif"

    if any(phrase in content for phrase in fight_triggers):
        return fight_response()

    if any(phrase in content for phrase in how_are_ya_triggers):
        return "Good'n you?"

    if "to be fair" in content:
        return "https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/to_be_fair.gif"

    if "toughest guy" in content:
        return "https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/img/end_of_the_laneway.jpg"

    if "appreciates" in content:
        return f"Take about 10 to 15% off'er there, <@{member_id}>"

    if any(word in content for word in ["great idea", "good idea"]):
        return "It's the best fuckin' idea I've ever heard in my life."


async def shoresy_response(member_id: int, guild_id: int) -> str:
    """Generates a response for the "fuck you shoresy" trigger phrase"""
    with open("./data/quotes.txt") as f:
        r = f.readlines()

    selection = random.choices(r, k=5)
    selected = random.choice(selection)

    second_mention = await query.get_random_member(member_id, guild_id)

    if second_mention is None and "{second}" in selected:
        return await shoresy_response(member_id, guild_id)

    return selected.replace("{second}", f"<@{second_mention}>").replace(
        "{mention}", f"<@{member_id}>"
    )


def fight_response() -> str:
    """Generate a response for the 'what's gunna happen' trigger phrase"""
    with open("./data/fight.txt") as f:
        r = f.readlines()
    return random.choice(r)
