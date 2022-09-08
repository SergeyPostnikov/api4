import telegram
import os

from dotenv import load_dotenv


if __name__ == '__main__':  
    load_dotenv()
    auth_token = os.getenv('TELEGRAM_API_KEY')
    bot = telegram.Bot(token=auth_token)
    print(bot.get_me())
