import telebot
from logic import *
from telebot import types

TOKEN = "7255599355:AAF46TE7ts6jP5zUAnnx_l-_aO3BG9hEX_8"

bot = telebot.TeleBot(token=TOKEN)



@bot.message_handler(commands=['start', 'restart'])
def start_func(message):
    print(f"USER INFORMATION:\n*UserId:{message.chat.id}\n*Username:{message.chat.username}")
    bot.send_message(chat_id=message.chat.id,
                     text="Привет, я бот, который может проанализировать любой текст, отправь мне текст(без абзацов) и я расскажу о нём, всё, что знаю"
                     )

@bot.message_handler()
def analyse(message):
    print(f"!!**{message.text}**!!")
    bot.send_message(
        chat_id= message.chat.id,
        text= wordsbynum(message.text)
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=alphabet(message.text)
    )

bot.polling(non_stop= not False)
