from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "5005266266"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://kiw:kiw@cluster0.ysa9qt4.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6450300940:AAHSmYRzuiEMIAc3Rw0EUr6RSI6wM6C1yhg")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/peler")
CMD_HNDLR = getenv("CMD_HNDLR", "")
PREFIX = CMD_HNDLR.split()
SESSION1 = getenv("SESSION1", "BQADMVMAELHXNWhmqGowU1t-ttSSsgcVD3jBCw-ThSfPNEfmDTw_ptkx9XUNp1rAsQIKwqoIrNOjSsjeKqiHtoDAN3ue_u8J6tpNqbgQLNbOX2Q7tVel3XzzPPDw585gLi9aiKa4RWzE-i6UzznyST5vGuzwT6I0BMQ1VNPH3klBL6LfhUyOdj5y044fLq2V6qDf4B3TijYy_eFgDRmvRZh9mtUmS0e9kLD8uGj3zJA67s3eTyy1kpzT0-aKvxAeQLDgVoBDtvBSa5Y-TMWlnMnjL4s0Oov5a8G3Ovu4eqs4n3FHxoilgOHgm18efhb0qdYXJuAo0ge3inGtY89ho0fQXG6GjwAAAAEqVk1aAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
