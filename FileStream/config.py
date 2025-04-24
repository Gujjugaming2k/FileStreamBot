from os import getenv

class Telegram:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")
    OWNER_ID = int(getenv("OWNER_ID", "7978482443"))
    WORKERS = int(getenv("WORKERS", "6"))  
    DATABASE_URL = getenv("DATABASE_URL")
    UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Telegram")
    SESSION_NAME = getenv("SESSION_NAME", "F2LxBot")
    FORCE_SUB_ID = getenv("FORCE_SUB_ID")
    FORCE_SUB = getenv("FORCE_UPDATES_CHANNEL", "false").lower() in ("1", "true", "t", "yes", "y")
    SLEEP_THRESHOLD = int(getenv("SLEEP_THRESHOLD", "60"))
    FILE_PIC = getenv("FILE_PIC", "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = getenv("START_PIC", "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = getenv("VERIFY_PIC", "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(getenv("FLOG_CHANNEL", "0"))  
    ULOG_CHANNEL = int(getenv("ULOG_CHANNEL", "0"))  
    MODE = getenv("MODE", "primary")
    SECONDARY = MODE.lower() == "secondary"
    AUTH_USERS = list(set(int(x) for x in getenv("AUTH_USERS", "").split() if x.isdigit()))

class Server:
    PORT = int(getenv("PORT", "8080"))
    BIND_ADDRESS = getenv("BIND_ADDRESS", "0.0.0.0")
    PING_INTERVAL = int(getenv("PING_INTERVAL", "1200"))
    HAS_SSL = getenv("HAS_SSL", "false").lower() in ("1", "true", "t", "yes", "y")
    NO_PORT = getenv("NO_PORT", "false").lower() in ("1", "true", "t", "yes", "y")
    FQDN = getenv("FQDN", BIND_ADDRESS)
    URL = f"http{'s' if HAS_SSL else ''}://{FQDN}/"

