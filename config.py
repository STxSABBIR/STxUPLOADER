import os

class Config(object):
    # Get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    # The Telegram API things.
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # The download location, where the HTTP server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # Chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # Default thumbnail to be used in the videos
    # Proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # Maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # Set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # Your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    SESSION_NAME = "STxUPLOADER"
    # Database URI (MongoDB)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER")
