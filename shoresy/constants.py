import os

try:
    import dotenv
except ModuleNotFoundError:
    pass
else:
    if dotenv.find_dotenv():
        print("Found .env file, loading environment variables")

        dotenv.load_dotenv(override=True)


FIGHT_TRIGGER = (
    "what's gunna happen",
    "whats gunna happen",
    "what's gonna happen",
    "whats gonna happen",
    "what's going to happen",
    "whats going to happen",
)

SHORESY_TRIGGER = ("fuck you shoresy", "fuck you, shoresy")

HOW_ARE_YA_TRIGGER = (
    "how're ya now",
    "how are ya now",
    "howr ya now",
    "how'r ya now",
)


class Config:

    token = os.getenv("DEV") if os.name == "nt" else os.getenv("TOKEN")
    sqlite_path = os.getenv("SQLITE")
