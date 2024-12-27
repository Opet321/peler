from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "5005266266"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://apem:apem@cluster0.iraog.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7885997455:AAH_pwhpzwBo37XdCUqVa_zpYeJnv7vOM4I")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/peler")
CMD_HNDLR = getenv("CMD_HNDLR", "")
PREFIX = CMD_HNDLR.split()
SESSION1 = getenv("SESSION1", "BQADMVMAUQ2svMD86If0IxbhqL1EbxLmJvN-Je_znwqvMoBL589RHTcHdPxC-LyjsaQwSE8rnOm8CqiVTiXnfZvkHKx7Rq18rq7atJmPOaorewPQyynsW5F-rCgoidWfg6x0M6jdF2iFZZm9WNZX_CO3GkTEfJQCLNmy6zMg6EQZ-M_hz1FRieP18E6K8J8pgsq6hYuinUYrIjTn1LFLJG6vL5cFOlozZpDi8V_EZ1_1RUngY_BavD3pRbZHHbgNyaJkXeqVthynpBJm0NIdCaEMFJQM8eoVxYbLrfNfmUFlUbkQPTmK05tifE9wY8TCahfYzraAXWtYfBWX26NfJZzFbbzeIwAAAAGsJH4uAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
