from os import getenv, environ
import requests

from dotenv import load_dotenv

DEV = False

load_dotenv()

TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN') if DEV else environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = getenv('TELEGRAM_CHAT_ID') if DEV else environ.get("TELEGRAM_CHAT_ID")

def make_a_post(user_display_name: str, joined: bool):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    text = f"{user_display_name} has {'joined' if joined else 'left'} voice chat"
    params = {
        "chat_id": str(TELEGRAM_CHAT_ID),
        "text": text,
    }
    response = requests.get(url, params=params)

