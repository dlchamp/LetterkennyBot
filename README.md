# LetterkennyBot

## Description

Now includes best of Season 10 and the first season of Shoresy
A simple Discord bot written in Python using the Disnake wrapper for Discord.  This bot will monitor channels for specific phrases and respond to them with over 70 quotes from the show.

If you don't wish to self host, you can always just [invite me to your server!](https://discord.com/api/oauth2/authorize?client_id=873640710480486451&permissions=109568&scope=bot%20applications.commands)

### New Feature(s)
Using the "Fuck you, Shoresy" hot phrase will add your Discord ID to a database. This database is only used to randomly select a member to replace "Reilly" or "Jonesy" in quotes where both characters would be roasted by Shoresy.
Users will be able to remove their ID from this database if they wish with a simple `/remove` command.
(*Quote Example: "Fuck you, `@Reilly`. Your mum sneaky gushed so hard she bucked me off the waterbed last night. Don\'t tell her I was thinking about `@Jonesy\'s` mum the entire time."*)


## Bot Usage

### Phrases the bot responds to
"Fuck you shoresy and a few others!

### Commands
 - `/remove` - Remove the user's Discord ID from the database
 - `/help` - Display the help embed with trigger info, data usage, and commands

## Self Hosting

### Dependencies

* Built on [Python3 - 3.9+](https://www.python.org/downloads/)
* get started quickly with `poetry install` from within the project root
* get poetry with `pip install poetry`

### Getting Started

#### Setting up Discord Bot
1. Login to Discord web - https://discord.com
2. Navigate to Discord Developer Portal - https://discord.com/developers/applications
3. Click *New Application*
4. Give the Application a name and *Create*
5. Add image for Discord icon - https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/container_icon.png
6. Go to Bot tab and click *Add Bot*
7. Keep the default settings for Public Bot - *checked* and Require OAuth2 Code Grant - *unchecked*
8. Add bot image - https://raw.githubusercontent.com/dlchamp/LetterkennyBot/main/container_icon.png
9. Copy Token
10. Go to OAuth2 tab
11. Under *Scopes* - Check Bot and applications.commands (needed for slash commands)
12. Under *Bot Permissions* - check Send messages, Attach Files, Read Message History, View Channels
13. Copy the generated link and Go to the URL in your browser - Invite Bot to your Discord server


#### Windows Installation and Run
1. Download this repo and extract to a location
2. Open command and navigate inside of bot's directory
3. Open the .env-sample file in a text editor and paste in your copied token, save, and rename the .env-sample to .env
5. Create your virtual env and install dependencies with `poetry install` from within the project's root directory (where main.py is located)
6. Run the project with `python main.py`


&nbsp;
___



## Version History

* 2.1
    * Updated to Disnake 2.5.1
    * Migrated to Poetry for dependency management
    * Migrated from JSON to SQLite for member list
    * Restructure and rewrote most of the project.
    * Added 10+ new quotes plus some from Shoresy season 1
    * Migrated to slash commands from the prefixed context commands
    * Formatted with Black
    * Updated scopes and permissions for in-app invite authorizations to support slash commands

* 2.0
    * Restructured and reorganized files and functions. - separated many functions out of main.py
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
