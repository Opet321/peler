from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "16712780"))
OWNER = int(getenv("OWNER", "6190309715"))
API_HASH = getenv("API_HASH", "7941450f5313966647b6d6fde5f933dc")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://apem:apem@cluster0.iraog.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7647918583:AAFRli68VM40AJJk_7-L4XZ2m5NFGDbSzU0")
OPENAI_API = getenv("OPENAI_API", "") 
FORUM_CHAT_ID = getenv("FORUM_CHAT_ID", "-1002314627378")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/peler")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
PREFIX = CMD_HNDLR.split()
SESSION1 = getenv("SESSION1", "BQD_BEwADxceS3dCW3WdAlXl1MUZBMkeEA4-_nVw3nloJsARDDl35R-2vFhwci1S3CfJ5q_2ZLi7pIELSnmdboOPM2nLBgyThNkh9xETbROXdvIwSEacoBlBgXZZah3Neviow3GJ9kIJf-lDVsbLhokB83xjJyMAZ5gawWmpchtIHuAv8ax-cbICqPuo3iFl_F-m4muYniQaxSlE-LL5w_8ta3NctvRn0PaxCBVmgqwyzcDx5hRERYHGtyiBZeR7oODnMvqiy4H9INDWPgPqqsrquC91OT2_a57p-1WL4EUDmJpN9Tg5v-UTED9wbAy65D_lglxJTeYtUUt_g9OxvSx3VHVkaAAAAAFw-KFTAA")
SESSION2 = getenv("SESSION2", "BQADMVMAaoM_OXT8rlfmQIpur71qsmjUkWX2J2SUfFEEiXHaJZisn_JweRbSrTE74JPBdnFm9cNkLS2-oLZyppGXKB-CJ6FYhl1-hJ5lt13-TrNjdalWnefWDUT6SgvenJ6DVz8XDIFB59ehHN02qgWmM41cNLUK6psfY5SqR5dUKyUnZKShlO-pZf5nfJraiQV80H1bP_XIIdiBv12J90l4SBlBwvVENyJjeuWf0RFEJ899l5h_krHjpgNlihhcCLriclazF-_hhUNlDqtWZQlkLV0LPfGSXjsEy1kVGWV5o_DB5jw-2EhBQzPv0DBe-chOknsDZXE5Do1nSac2rxcvWzQ3AQAAAAGgmQagAA")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
