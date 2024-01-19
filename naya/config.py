from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "209235"))
OWNER = int(getenv("OWNER", "5222322204"))
API_HASH = getenv("API_HASH", "169ee702e1df4b6e66d80311db36cc43")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://kiw:kiw@cluster0.ysa9qt4.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6450300940:AAHSmYRzuiEMIAc3Rw0EUr6RSI6wM6C1yhg")
OPENAI_API = getenv("OPENAI_API", "")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
BRANCH = getenv("BRANCH", "naya")  # don't change
REPO_URL = getenv("REPO_URL", "https://github.com/opet321/memek")
CMD_HNDLR = getenv("CMD_HNDLR", "")
PREFIX = CMD_HNDLR.split()
SESSION1 = getenv("SESSION1", "BQADMVMAYVfwZa1vxANT0hxb973rAiIeG0IS1Vx-ShtnmkfnZKCekHFLjgv6K8NxwrOn36UfPEdERJvbz36FEJju4a7fx_aIEtmWa2_JCbxIj8BZs7d9ChKvR8HjP5wVOvHjAjvrpHZn39ZtekalsbMir2OEnc1t-gURpRe5dQZdoZDStKX00SPnLtHOn9TJx6dOPaq91q-9_Ahqtqa0hgaxfy9S2JzbCpGoEgW6nnYlo3rEWnV2fa89eRFv1XHSR5amrerQRIwsRA5uzeHTYuqtxZq0llZZIv1rHcZ21fiPUwMIgfq9MetmAqJ1N7sedYubQlUt4NtEKIswe-URgztYka9ANwAAAAE3RlAcAA")
SESSION2 = getenv("SESSION2", "BQADMVMASBimmq3C54x1OvLPcAuCG57koEqVKXobwF9PoL802PxLvkh2dR3K5VE_3lA8pwx8j8L6LIE-NR5IL_6xR7UfjaPExOAT8PaWR4eRlA-8rjMMwF82R6AUPwDJXajVmgjPfrEFzyUQo6eUobuUQEJbbTgtCSqFNqubdeigLJDwDtOlsq20WeIsDbMEfsin0fj40tkQ7rUnWYP2I_edq8mB12e1uu1sVhFPiiybrL5b3KUv2dsIpb_ek6BCHOyPvwGGjLqsas7hHYRQHtkb-VgO3OR3w8c99exGRbvIe5arrtCrRSxEUmTE44BaLTAtVVr4WlD3ZYyEIQ-ceXDj250pbQAAAAB3xoqMAA")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
