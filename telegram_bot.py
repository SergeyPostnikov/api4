import telegram
import os

from dotenv import load_dotenv


if __name__ == '__main__':  
    load_dotenv()
    auth_token = os.getenv('TELEGRAM_API_KEY')
    bot = telegram.Bot(token=auth_token)
    # print(bot.get_me())
    # updates = bot.get_updates()
    # print(updates[0])
    bot.send_message(text="Let's the game begin", chat_id=-1001691456773)
