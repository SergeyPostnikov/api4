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
    chat_id = -1001691456773
    # bot.send_message(text="Let's the game begin", chat_id=chat_id)

    bot.send_photo(chat_id=chat_id, photo=open('images/BlackHole_Simonnet_960.jpg', 'rb'))
    # i don't f@@n know where in that docs this method
    # 'goto' is best way to find something what you need
    