#(©)NovaXTG




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6216796862:AAEzPKNRdhnpdGfCoGmwHchBDGwxuZT2p1Q")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9321645"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6a1b5084e59012093525c2443880a09a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001840703856"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5296610774"))

#Port
PORT = os.environ.get("PORT", "8080")

#Shortener
SHORTENER_WEBSITE = os.environ.get('SHORTENER_WEBSITE', 'tnshort.net')
SHORTENER_API = os.environ.get('SHORTENER_API', 'a99608641893c27e95a317a55d13112c9833cae7')
#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://karthickjk:karthick@cluster0.vcjskkq.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "mona)

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001856308530"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hᴇʟʟᴏ {first}🦋 ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ Fɪʟᴇ ᴛᴏ ʟɪɴᴋ + ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ⚡️</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5296610774 1232844084").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Pʟᴇᴀsᴇ ɪᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ❗️</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>ɴᴀᴍᴇ</b> : {filename}\n\n ɴᴏᴛᴇ: ᴀꜰᴛᴇʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ꜰɪʟᴇꜱ, ꜱᴀᴠᴇ ᴛʜᴇ ꜰɪʟᴇ ᴛᴏ ɢᴀʟʟᴇʀʏ ᴀɴᴅ ᴄʟɪᴄᴋ ᴛʜᴇ ᴅᴇʟᴇᴛᴇ ʙᴜᴛᴛᴏɴ, ᴅᴏɴ'ᴛ ᴄʟɪᴄᴋ ʙᴇꜰᴏʀᴇ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇ ꜰɪʟᴇꜱ, ɪꜰ ᴜ ᴅᴏɴ'ᴛ ᴡᴀɴᴛ ᴛʜɪꜱ ꜰɪʟᴇ ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴅᴇʟᴇᴛᴇ ʙᴜᴛᴛᴏɴ")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

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
