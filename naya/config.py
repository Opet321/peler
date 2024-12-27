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
SESSION1 = getenv("SESSION1", "BQADMVMAGdxT4e21Rve5lYOPuhK7Ns7wUxnFBuTj99FDOBwN60rw6gDTGyuuoqeIJS4tjxcMKChqSO7_9e3gQFoI2Wnk-XC-UbdzpMTGhMdCaQN9QlcEW8vKhVVVhgKlJhbaA9Ztyuvo1pp-hDFXeI0_SBmMYojjuR2su2But7QWjjTYDjAct8VgIvmvA6oCZgbOA3K_xzLoN1Wyapd0xAJTRZ1z5pCzSHZjaA47KoJSYWeDyYXweGXuGLeCIv7RstjsXgP58GD0toG7XISvE5unStO-WnU8KxKnQVd8sPjLIbxrEPtJPlbqChvPhpeAi0hH_tVcjq4pQle90hUHUgzw1E3I6gAAAAHYqPKNAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
