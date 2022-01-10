# LetterkennyBot

## Description

Now includes best of Season 10 Shoresy!
A simple Discord bot written in Python using the Nextcord wrapper for Discord.  This bot will monitor channels for specific phrases and respond to them with over 40 quotes from the show.

If you don't wish to self host, you can always just invite me to your server!  
https://discord.com/api/oauth2/authorize?client_id=873640710480486451&permissions=117760&scope=bot

### New Feature(s)
Using the "Fuck you, Shoresy" hot phrase will add your Discord ID to a database. This database is only used to randomly select a member to replace "Reilly" or "Jonesy" in quotes where both characters would be roasted by Shoresy.
Users will be able to remove their ID from this databse if they wish with a simple `-remove` command.
(*Quote Exmample: "Fuck you, `@Reilly`. Your mum sneaky gushed so hard she bucked me off the waterbed last night. Don\'t tell her I was thinking about `@Jonesy\'s` mum the entire time."*)


## Bot Usage

### Phrases the bot responds to
1. "Fuck you shoresy" (most variations)
2. "What's gunna happen?" (most variations)
3. "Fucking embarrassing"
4. "How are ya now"
5. "To be fair"
6. "Toughest guy"
7. "Happy birthday"
8. That's "what I appreciates" about you (quoted section is what's being checked - complete sentence isn't required)

### Commands
 - `-remove` - Remove the user's Discord ID from the database

## Self Hosting

### Dependencies

* Built on the latest [Python3 - 3.9.7](https://www.python.org/downloads/)
* see requirements.txt for Python dependencies
* Python installed with PATH access in Windows

### Getting Started

#### Setting up Discord Bot
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


#### Unraid Docker Installation and Run
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
12. Key - *paste your token*
13. Value - paste token from Discord Developer Bot you created earlier in **Setting up Discord Bot - step 7**
14. *Add*
15. *Apply* - Image will be pulled, container will build and start automatically.
16. Profit.

#### Windows Installation and Run
1. Download this repo and extract to a location
2. Open command and navigate inside of bot's directory
3. Open the .env-sample file in a text editor and paste in your copied token, save, and rename the .env-sample to .env
4. Run `python -u main.py`


&nbsp;
___



## Version History

* 2.0
    * Resctructed and reorganized files and functions. - seperated functions out of main.py
    * Added JSON "database" for storing Discord member IDs for quotes with 2 `@mentions`
    * Added `-remove` command to allow users to remove themselves from the database.
    * Added back the `-help` command. Includes data usage disclaimer
    * All changes since 1.4 have been pushed into this update.

* 1.4
    * Updated quotes.txt to include the best of Season 10 Shoresy!

* 1.3
    * Formatted following PEP8 guidelines
    * Migrated to Nextcord
    * Moved to using github links to gifs as sending the file appears to slow responses slightly vs just submitting a link and letting Discord display the animated file.

* 1.2
    * Added -help command to display phrase the bot is listening for.

* 1.1
    * Added more quotes, removed "Happy birthday" on_message since it was spamming when multiple members were wishing someone "Happy Birthday"

* 1.0
    * Initial commit.
