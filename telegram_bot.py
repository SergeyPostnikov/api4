import telegram
import os
import time
import random
import requests

from dotenv import load_dotenv


def get_random_picture(directory):
    *args, files = next(os.walk(directory))
    random.shuffle(files)
    return f'{directory}/{random.choice(files)}'


if __name__ == '__main__':
    load_dotenv()
    auth_token = os.getenv('TELEGRAM_API_KEY')
    period = os.getenv('PUB_PERIOD_HRS')
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
