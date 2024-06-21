import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "EMAIL": os.environ.get("EMAIL"),
    "PASSWORD": os.environ.get("PASSWORD"),
    "USERNAME": os.environ.get("USERNAME"),
    "USER_AGENT": os.environ.get("USER_AGENT"),
}
