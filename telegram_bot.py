import telegram
import os
import time
import random
import requests

from dotenv import load_dotenv
from os.path import join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def get_random_picture(directory):
    *args, files = next(os.walk(directory))
    random.shuffle(files)
    return join(directory, random.choice(files))


if __name__ == '__main__':
    load_dotenv()
    auth_token = os.environ['TELEGRAM_API_KEY']
    period = os.getenv('PUB_PERIOD_HRS', default=4)
    chat_id = os.getenv('CHANNEL_ID')

    bot = telegram.Bot(token=auth_token)

    while True:
        with open(get_random_picture('images'), 'rb') as f:
            photo = f.read()
        
        try:
            bot.send_photo(chat_id=chat_id, photo=photo)
        except telegram.error.NetworkError as err:
            print(err)
            time.sleep(5)
            continue
        except requests.exceptions.ConnectionError as err:
            print(err)
            time.sleep(5)
            continue
        else:
            time.sleep(3600 * int(period))
