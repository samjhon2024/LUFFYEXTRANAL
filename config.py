"""
from os import getenv


API_ID = int(getenv("API_ID", "26074242"))
API_HASH = getenv("API_HASH", "e68320b3f73cbc927b97be3cf9192fdd")
BOT_TOKEN = getenv("BOT_TOKEN", "7193218982:AAFIo-2qFLc-i2mbQYcKALB1S2mRAmQxUQU")
OWNER_ID = int(getenv("OWNER_ID", "6804641253"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7095754403 7383598092").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://Rajahd41:Rajahd41@cluster0.omrv9cu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002060207860"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002060207860"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

