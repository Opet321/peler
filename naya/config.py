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
SESSION2 = getenv("SESSION2", "BQADMVMArWxTovD7MkHOT_loa0PisWi5GMliSCRgh4SqlPuzTsh1V7NV6i6-km2I5bDmhAVYA_wBzEBnQznnehaCr_V46RZq8bokWKr-QzxBBrNZ-Q457k4AAZPV1FBXEUvYz8NJUVoZbqq-98mnx6eSwSywR0LMusHz_bX5Hw1nm8tof42glCrc3cidXtQ2rdGeud92lIlyQ2rGpVjAs8TFqB_2FDi5b1hIBPti1BIi3GRdP2cyRANGBjd9CN9Pd4ZzlDYuGIVY0fz09YICLHO8af00ohOUif9PHaWlSFnkK56HnYuqbXq1FV3ZFR2bKC4mGtRZHNFeUKFPPZ9t5MAZGO9PmQAAAAFPejahAA")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
