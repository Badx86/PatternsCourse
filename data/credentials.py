import os
from dotenv import load_dotenv

load_dotenv()


class Credentials:
    # $env:STAGE="prod"; $env:BROWSER="chrome"; python data/credentials.py
    if os.environ["STAGE"] == "prod":
        LOGIN = os.getenv("PROD_LOGIN")
        PASSWORD = os.getenv("PROD_PASSWORD")
    # $env:STAGE="qa"; $env:BROWSER="chrome"; python data/credentials.py
    elif os.environ["STAGE"] == "qa":
        LOGIN = os.getenv("QA_LOGIN")
        PASSWORD = os.getenv("QA_PASSWORD")


print(Credentials.LOGIN)
print(Credentials.PASSWORD)
