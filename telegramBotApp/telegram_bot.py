# start Django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django

django.setup()
# end start Django

import telebot

from app.settings import API_TOKEN
from telegramBotApp.services import *

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Get answer to bot user with user's SuperCode
    :param message: message user
    :return: None
    """
    unique_code = extract_unique_code(message.text)
    if unique_code:  # if the '/start' command contains a unique_code
        code_is_valid = check_code_valid(unique_code)
        if code_is_valid:
            super_code = get_super_code(message.from_user.username)
            reply = f"Приветствую {message.from_user.first_name}! Твой уникальный код - {super_code}."
        else:
            reply = "Что-то пошло не так - не валидная ссылка. Спробуйте ще раз"
    else:
        reply = "Вы не можете начать использовать бот без реферальной ссылки. " \
                "Перейдите в бот с помощью реферальной ссылки."
    bot.reply_to(message, reply)


bot.infinity_polling()

# for test bot
if __name__ == '__main__':
    pass
