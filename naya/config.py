from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "6190309715"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://apem:apem@cluster0.iraog.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7941016224:AAHGa6TSL6ppCOs5_Th1et-NwIogHAO5snA")
OPENAI_API = getenv("OPENAI_API", "") 
FORUM_CHAT_ID = getenv("FORUM_CHAT_ID", "-1002314627378")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/peler")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
PREFIX = CMD_HNDLR.split()
SESSION1 = getenv("SESSION1", "BQD_BEwAj26J42I_bgsiD1VsxAURMDeL8CDDe3x1K6sFeXlzQZ_jjiRdErsB1LTycPsKY5GOVM38tySqA-_c3ihzBmnS8lo7hzEuHbVNveFZ0Iikgf1yyK7OD1naR2lAp_sxuTSODYMgSU1ebJkMq_YooVqALDthRcIDWdIoh2k17UTlN7lgE0aWnWdLprpiSwqql7tZUE4TwcvNDPlaaXC34ArVZ82t28DYxZc9CSF8h7-nh3apFOtmTglAe7N5g6EXFF91p_ea_Fr3YjU0k7l3_otHA5zJN1DLjnRjGiRslByzDtLeO8mvp6sN8qJ2EN-hw82JmTFJHiggOtSgwhhaL-LwvgAAAAFw-KFTAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
