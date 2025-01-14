from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "16712780"))
OWNER = int(getenv("OWNER", "5628376737"))
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
SESSION1 = getenv("SESSION1", "BQD_BEwAXPDsQTHf-r4E25RviN6QmSlpZW4LtuHhCExYvF1mqj5JMipNOJ8Qwi1MQXSASoDGNJ9bSB8gAYHuNod7T4v2z9VLnZDZtXbQcEVizCiQqPJI-Ls823CzVdv5uegHyppJ-Mmsku6DG0kmFt2kxtT57xUj2vGn_TJstzad3ocETm82Q9WLyV86UB-C4QB3KqQDwUuEBBVIXsRzUINMow4V7ojT9g9b3q2PNrr-emUcpNZGfAHy3NyjFZ_hlMjm2uYXvUgziltdgq5IdU4D-kg6XoIgRcAeQLcqoTRVqpLeNA8F0dLRfG-u3XaAfr3cquf-NaoTjCFsMhyUSO7sfahWRQAAAAFw-KFTAA")
SESSION2 = getenv("SESSION2", "BQADMVMArWxTovD7MkHOT_loa0PisWi5GMliSCRgh4SqlPuzTsh1V7NV6i6-km2I5bDmhAVYA_wBzEBnQznnehaCr_V46RZq8bokWKr-QzxBBrNZ-Q457k4AAZPV1FBXEUvYz8NJUVoZbqq-98mnx6eSwSywR0LMusHz_bX5Hw1nm8tof42glCrc3cidXtQ2rdGeud92lIlyQ2rGpVjAs8TFqB_2FDi5b1hIBPti1BIi3GRdP2cyRANGBjd9CN9Pd4ZzlDYuGIVY0fz09YICLHO8af00ohOUif9PHaWlSFnkK56HnYuqbXq1FV3ZFR2bKC4mGtRZHNFeUKFPPZ9t5MAZGO9PmQAAAAFPejahAA")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
