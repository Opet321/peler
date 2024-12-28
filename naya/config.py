from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "5005266266"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://apem:apem@cluster0.iraog.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7620839975:AAHxITmSgT_6SD-TwT9CKGP_hveL8R4WkEI")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/peler")
CMD_HNDLR = getenv("CMD_HNDLR", "")
PREFIX = CMD_HNDLR.split()
SESSION1 = getenv("SESSION1", "BQADMVMArdYrEiTZEmgwbxUXzW9HgJLQ4-Wyn9Xa3v7ErAptdeir9Xbj1IVXj_FKUNxwq3PcXv8om-LqBTFjVwinDY3KCi2PbuyW8FTBajlp7nJjDJxeEJvw-Qloa7aRGWBSEOiKBACyM_xw_t9pB_9JbKoV2UcrKekMd73aU86V9BIbAXdCIT5O0hB-GO_2J8B9scYU2F3M2RPuHm7gVq8bWvPEFnYhO-NHgTUFedy5erF5K7Q1up1cF9IHZgjSBFlMJHxWIgLDMGhyuE1PgahI1hIWdHYXgDyhYl381GyJ6X3PoBf3DPdZ1oOa71jGjWJ71Q2uBPd3bvph9L0RT49YQ7SLfwAAAAFPejahAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
