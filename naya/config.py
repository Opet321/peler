from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "5005266266"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://apem:apem@cluster0.iraog.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7764544491:AAEuyGkR8DNvqLjktcb6CJlH2xpFKnENQpo")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/peler")
CMD_HNDLR = getenv("CMD_HNDLR", "")
PREFIX = CMD_HNDLR.split()
SESSION1 = getenv("SESSION1", "BQADMVMAI13dkKxLh40XLo-xV77Q2GKH9o5Hy-RKpvRTnGTaddWJi31Kmi3jn9sAtzp-cZ-U7Zv0ONRlKqtJ7ULELzpMNXENG2wgOKIEgxoxDl7hIq_gVpSJ89GutrX6kjHnFbMS395RX3SXaedvp7NFoaXWIr7Om50lrzSMLS3bD_iVLq_xVuZTWAVJXUHK-oCiuda5FXxSttXtFaJQBSWaNlT5gI0MuCO3h-07ugkF5UbQ7HcJnFRj6hrGmiZ0I1o3EH8AuFRSnl4I8l2tMEUTpSWnS-QqRTtXv-5qwVek8Jy0wXtgnk0L1NkAE6A15LYc03L_8tUVEadY1Fub3Ik0RdsUNAAAAAHYqPKNAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
