from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "5628376737"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://apem:apem@cluster0.iraog.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7620839975:AAHxITmSgT_6SD-TwT9CKGP_hveL8R4WkEI")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/peler")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
PREFIX = CMD_HNDLR.split()
SESSION1 = getenv("SESSION1", "BQADMVMAG4LLZQZpA7rHHYHp62PJ9-nRDeRmC6oo4kgg1bT3-0G3GryEQmtCjHoIF9uyJvhTLnDAX-u9pFuZe1FTMktxN_oMTRjR8y1D-SqsVDGBZ_Oi_YnjlmO8HoMxx-FANDBeMuQdWsf2ICVXKTeJwCkxHk1UFD7gT2qq28D33-0JGqmhrIqZrwzfS3uVDcODUY_9Fk_VZO_Cq0dUaTS43GQ5t3a7NL2-0o2v4DGB45mw45l8t2UnAEAvARee25FXoXm_MlhPn9xMCSAJCcklCuJe4ZkRu9O_YMgxLOBZkSRvElmY8MQcA0ulU5s8nMKEBFzd4mA0JKSv_WJStfXk5xz_rgAAAAFPejahAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
