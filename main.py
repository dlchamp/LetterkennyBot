from os import getenv

from letterkennybot import bot


def main():
    bot.run(getenv("TOKEN"))


if __name__ == "__main__":
    main()
