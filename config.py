import os

API_ID = API_ID =  25891183

API_HASH = os.environ.get("API_HASH", "36709c81d7609a81f86de931cbc87f3a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6677611444:AAG1b6eR2LfUDhbqaiHdpRbslo3FHIbfpgY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6200203086))

LOG = -1001605524352,

# UPDATE_GRP = -1002168262667, # bot sat group

# auth_chats = [-1002235760775]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6200203086").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


