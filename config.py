#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7264446075:AAGDKrAIcWm7rYTZKabW5p-NN-jv7i3R2PY")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22207976"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5c0ad7c48a86afac87630ba28b42560d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001871887219"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6977991334"))

#Port
PORT = os.environ.get("PORT", "8006")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://letsearn:fakefacebook602@cluster0.o0trvz0.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>.   𝗔𝗻𝗶𝗺𝗲 𝗶𝗻 𝗛𝗶𝗻𝗱𝗶 👇👇\nhttps://t.me/+2fsV4nzHvOs2OGNl\nhttps://t.me/+2fsV4nzHvOs2OGNl\n\n  𝗔𝗻𝗶𝗺𝗲 𝗖𝗵𝗮𝘁 𝗚𝗿𝗼𝘂𝗽 👇👇\nHTTPS://T.ME/DKANIME_GROUP\nHTTPS://T.ME/DKANIME_GROUP\n\n  𝗔𝗱𝘂𝗹𝘁 𝗔𝗻𝗶𝗺𝗲 𝗶𝗻 𝗵𝗶𝗻𝗱𝗶 [𝟭𝟴+] 😍👇👇\nhttps://t.me/+X-vfMcD-GkY3MzQ1\nhttps://t.me/+X-vfMcD-GkY3MzQ1</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7453879429").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>🍑 𝗔𝗱𝘂𝗹𝘁 𝗔𝗻𝗶𝗺𝗲 𝗶𝗻 𝗵𝗶𝗻𝗱𝗶 [𝟭𝟴+] 🤠 https://t.me/+X-vfMcD-GkY3MzQ1 https://t.me/+X-vfMcD-GkY3MzQ1</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(6872968794)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
