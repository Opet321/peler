from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "5005266266"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://kiw:kiw@cluster0.ysa9qt4.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6604729291:AAGhS6vv1v4YT_vM9HrHECMGC2LXzJitXnY")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/peler")
CMD_HNDLR = getenv("CMD_HNDLR", "")
PREFIX = CMD_HNDLR.split()
SESSION1 = getenv("SESSION1", "BQADMVMAhCgaeE36SrUziqgxKwxJBZSPS6ZhcM6PZ2Gp5hq8dF4JHqzat9-wvnrV2YHTKXakSNEmC1ZoO8WLLf_nkOTekmtRmkEX-PVDWNxDtmEuHu7rgxiBwjgytBofcTmkJDUpkAOljtRCr4lTGVKiwtYvqF9lfvT5OnjIl9uufgBTkU73hmvjmSmOtrm1E6X0wu4w_XPqkAYqrI9ISDmIaSGbeVTIKJ_HQeAX4GdzgBTBde-RrBoct641-nTgPqITVEnW73QM9MDgrwe0wTb_g49Ke6Td7wARv5FtdvkKvJe342cFxO66h9q_dS9Pi-EylN1s3Eo4muFJuXvFGTKjsj2qygAAAAHYqPKNAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
