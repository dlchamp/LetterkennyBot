# LetterkennyBot

A simple Discord bot written in Python using the Nextcord wrapper for Discord.  This bot will monitor channels for specific phrases and respond to them with over 40 quotes from the show.

## Description

As part of my Python learning experience I wanted to try my hand and building a discord bot that could also be ran in Docker since I use unRAID.
My friends and I are pretty big Letterkenny fans and we've come across a couple Discord bots based around quotes from the show, specifically Shoresy, but they   
seemed to be lacking a lot of the quotes, and missing other features to make the bot more fun.  I decided to improve on this idea by including 40 quotes from Shoresy (will be updating as more seasons come out.)
This is the very first project I've ever completed in Python and I'm sure that the code would be cleaner and more optimized, but it does work well in it's current version and I will be updating and optimizing
as I hone my knowledge and skills.



## Using the bot
* Bot responds to "Fuck you shoresy" (any variation) - will respond with a randomly selected string located in quotes/quotes.txt, mentions user that invoked response
* One response will include "Fight me, see what happens" - user can then respond with "What's going to happen?" (or any variation) and will be replied to with a  
with a randomly selected quote from quotes/fight.txt
* Bot responds to "to be fair" (any variation) with To_be_fair.gif (scene from show)
* Bot responds to Birthay wishes with super soft birthday gif - has 10 minute cooldown to prevent spam on multiple birthday wishes in quick succession.
* Bot reponds to "Fucking embarrasing" (any variation) with trashcan kick .gif
* Bot responds to "toughest guy" (any variation) with end_of_the_laneway.jpg


### Dependencies

* Built on the latest [Python3 - 3.9.7](https://www.python.org/downloads/)
* see requirements.txt for Python dependencies
* Python installed with PATH access in Windows

## Getting Started

**Setting up Discord Bot**
1. Login to Discord web - https://discord.com
2. Navigate to Discord Developer Portal - https://discord.com/developers/applications
3. Click *New Application*
4. Give the Appplication a name and *Create*
5. Add image for Discord icon - https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/container_icon.png
6. Go to Bot tab and click *Add Bot*
7. Keep the default settings for Public Bot - *checked* and Require OAuth2 Code Grant - *unchecked*
8. Add bot image - https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/container_icon.png
9. Copy Token
10. Go to OAuth2 tab
11. Under *Scopes* - Check Bot
12. Under *Bot Permissions* - check Send messages, Attach Files, Read Message History, View Channels
13. Copy the generated link and Go to the URL in your browser - Invite Bot to your Discord server


**Unraid Docker Installation and Run**
1. Navigate to Docker tab
2. *Add container*
3. Give it a name - "LetterkennyBot"
4. Expand Advanced view
5. Add repo - dlchamp/letterkennybot
6. Add dockerhub url - https://hub.docker.com/r/dlchamp/letterkennybot
7. Add icon url - https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/container_icon.png
8. Leave network type as Bridge
9. *Add another Path, Port, Variable, Label or Device
10. Switch config type to *Variable
11. Name - TOKEN
12. Key - TOKEN
13. Value - paste token from Discord Developer Bot you created earlier in **Setting up Discord Bot - step 7**
14. *Add*
15. *Apply* - Image will be pulled, container will build and start automatically.
16. Profit.

** Windows Installation and Run**
1. Download this repo and extract to a location
2. Open command and navigate inside of bot's directory
3. Open the .env-sample file in a text editor and paste in your copied token, save, and rename the .env-sample to .env
4. Run `python -u main.py`

## Notes
- This should be able to be imported directly into Replit and ran without much hassle.  simply remove the `from dotenv import load_dotenv` line as it won't be needed,
then import your bot token into Replit per their [instructions](https://docs.replit.com/archive/secret-keys)


## Version History

* 2.0
    * Formatted following PEP8 guidelines
    * Migrated to Nextcord
    * Moved to using github links to gifs as sending the file appears to slow responses slightly vs just submitting a link and letting Discord display the animated file.

* 1.2
    * Added -help command to display phrase the bot is listening for.

* 1.1
    * Added more quotes, removed "Happy birthday" on_message since it was spamming when multiple members were wishing someone "Happy Birthday"

* 1.0
    * Initial commit.
