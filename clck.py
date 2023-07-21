import telebot
import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TG_TOKEN")

bot = telebot.TeleBot(TOKEN)

def is_url(url: str):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def getShortLink (url: str):
    response = requests.get('https://clck.ru/--', params = {'url': url})
    return response.text

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (is_url(message.text)):
        bot.send_message(message.from_user.id, getShortLink(message.text))
    else:
        bot.send_message(message.from_user.id, 'This in not a url!')

bot.polling(none_stop=True, interval=0)