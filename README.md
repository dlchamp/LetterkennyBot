# LetterkennyBot



## Description

As part of my Python learning experience I wanted to try my hand and building a discord bot that could also be ran in Docker since I use unRAID.
My friends and I are pretty big Letterkenny fans and we've come across a couple Discord bots based around quotes from the show, specifically Shoresy, but they   
seemed to be lacking a lot of the quotes, and missing other features to make the bot more fun.  I decided to improve on this idea by including 25 quotes from Shoresy (will be updating as more seasons come out.)  This is the very first project I've ever completed in Python and I'm sure that the code would be cleaner and more optimized, but it does work well in it's current version and I will be updating and optimizing as I hone my knowledge and skills.

## Known Issues
* Some responses will break if userlist/usernames.txt is left empty.  They will still respond, but variable "{random}" will be left in the response string
* There's currently over 20 responses to "Fuck you shoresy", but sometimes the responses might repeat more often than I'd like.
* Getting more familiar with python, docker, github, and dockerhub.  Will make improvements where possible over time.

## In Progress
* ~~**General** - Set cooldown for "birthday" response so that there's not a response for every "Happy Birthday" message within a short period.~~
* **General** - Set check for last message to prevent responses repeating too often.
* **Docker** - implement paths for access to userlist/usernames.txt to be able to edit outside of the container

## Using the bot
* Bot responds to "Fuck you shoresy" (any variation) - will respond with a randomly selected string located in quotes/quotes.txt, mentions user that invoked response
* One response will include "Fight me, see what happens" - user can then respond with "What's going to happen?" (or any variation) and will be replied to with a  
with a randomly selected quote from quotes/fight.txt
* A couple of the responses will have a second mention - these mentions must be configured in the userlist/usernames.txt file.
* Bot responds to "to be fair" (any variation) with To_be_fair.gif (scene from show)
* Bot responds to Birthay wishes with super soft birthday gif - has 10 minute cooldown to prevent spam on multiple birthday wishes in quick succession.
* Bot reponds to "Fucking embarrasing" (any variation) with trashcan kick .gif
* Bot responds to "toughest guy" (any variation) with end_of_the_laneway.jpg


### Dependencies

* Built on the latest [Python3 - 3.9.6](https://www.python.org/downloads/)
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

**Windows Installation and execution**

1. Download the latest Python3 from [python.org](https://www.python.org/downloads/)  
2. Download this project and unzip to a directory
3. Edit main.py and comment out (#)`token = os.environ['TOKEN']`, then uncomment (remove #) `#token = 'BOT TOKEN'`, then replace `BOT TOKEN` with your Discord bot token you copied during **Setting up Discord bot - Step 7**  
4. Save the changes
5. Navigate to userlist/ and edit the usernames.txt file - include your friends' discord IDs one per line - sample ID <@789651e579365>
6. Open command prompt and navigate to your LetterkennyBot-main folder (ex. cd :C:\Users\YOURUSER\Documents\DiscordBot\LetterkennyBot-main\)
7. Install dependencies - `pip install -r requirements.txt`
8. Run the main.py - `python main.py`
9. Profit.


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


