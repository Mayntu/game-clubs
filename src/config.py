from dotenv import load_dotenv
from os import environ
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


try:
    load_dotenv()
except Exception as e:
    log.error(f"failed to load dotenv : {e}")


class CONFIG:
    class CONN:
        HOST     : str = environ.get("DB_HOST")
        PORT     : int = environ.get("DB_PORT")
        PASSWORD : str = environ.get("DB_PASSWORD")
        USERNAME : str = environ.get("DB_USERNAME")
        DB_NAME  : str = environ.get("DB_NAME")
    class APP:
        NAME : str = "Game Clubs"
        VERSION : str = "0.0.1"

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{CONFIG.CONN.USERNAME}:{CONFIG.CONN.PASSWORD}@{CONFIG.CONN.HOST}:{CONFIG.CONN.PORT}/{CONFIG.CONN.DB_NAME}"
    },
    "apps": {
        "models": {
            "models": ["src.models.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}