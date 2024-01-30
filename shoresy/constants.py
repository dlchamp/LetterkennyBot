import os

from shoresy import log

logger = log.get_logger(__name__)

try:
    import dotenv
except ModuleNotFoundError:
    pass
else:
    if dotenv.find_dotenv():
        logger.info("Found .env file, loading environment variables")

        dotenv.load_dotenv(override=True)


FIGHT_TRIGGER: tuple[str, ...] = (
    "what's gunna happen",
    "whats gunna happen",
    "what's gonna happen",
    "whats gonna happen",
    "what's going to happen",
    "whats going to happen",
)

SHORESY_TRIGGER: tuple[str, ...] = ("fuck you shoresy", "fuck you, shoresy")

HOW_ARE_YA_TRIGGER: tuple[str, ...] = (
    "how're ya now",
    "how are ya now",
    "howr ya now",
    "how'r ya now",
)

GOOD_IDEA: tuple[str, ...] = ("great idea", "good idea")


DEV_MODE: bool = os.getenv("DEV", "true") == "true"


class Config:
    """Contain bot configuration."""

    _dev_token: str = os.getenv("DEV_TOKEN", "")
    _prod_token: str = os.getenv("TOKEN", "")
    sqlite_path: str = os.environ["SQLITE"]
    alembic_path: str = os.getenv("ALEMBIC", "")

    token = _dev_token if DEV_MODE else _prod_token
