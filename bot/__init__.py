import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("23225740"))
    API_HASH = os.environ.get("f671921d4107c9f350c15fd8d12687cc")
    BOT_TOKEN = os.environ.get("7037613682:AAHRedGZ291XlJF0KkD_ICdgcwANnuiXObA")
    BOT_USERNAME = os.environ.get("Baba_Vass")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
