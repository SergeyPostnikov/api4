import telegram
import os
import time
import random

from dotenv import load_dotenv


def get_random_picture(directory):
    *args, files = next(os.walk(directory))
    random.shuffle(files)
    return f'{directory}/{random.choice(files)}'


if __name__ == '__main__':
    load_dotenv()
    auth_token = os.getenv('TELEGRAM_API_KEY')
    period = os.getenv('PUB_PERIOD_HRS')
    bot = telegram.Bot(token=auth_token)
    chat_id = -1001691456773

    while True:
        bot.send_photo(chat_id=chat_id, photo=open(get_random_picture('images'), 'rb'))
        time.sleep(3600 * int(period))
