import json

import telebot
from threading import Thread
import requests
import time

token = "332111059:AAGI8_XicORXFMFrzxjQpb-LOqx9EUmdB8I"

bot = telebot.TeleBot(token)

users = set()

@bot.message_handler(commands=['image'])
def start_images(message):
    bot.send_photo(message.chat.id, "http://mironovacolor.org/articles/article_07/hora_5_sokrovish.jpg")

@bot.message_handler(commands=['music'])
def start_music(message):
    bot.send_audio(message.chat.id, "http://cdndl.zaycev.net/869165/4188966/%D0%91%D0%90%D0%A3%D0%B3%D0%BD%D0%B5%D1%82%D0%B5%D0%BD%D0%B8%D1%8F_-_%D0%93%D0%BE%D0%BB%D0%BE%D1%81+%D0%9E%D0%B2%D0%BE%D1%89%D0%B5%D0%B9+%28demo%29.mp3")


@bot.message_handler(commands=['spam'])
def start_spam(message):
    users.add(message.chat.id)
    bot.send_message(message.chat.id, "Берем сироп вишневый!")

@bot.message_handler(commands=['stop'])
def stop_spam(message):
    users.remove(message.chat.id)
    bot.send_message(message.chat.id, "Ок, все.")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        code = message.text
        #result = eval(code)
        result = "Выкуси!"
        bot.send_message(message.chat.id, str(result))

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "Чувак, ты пургу мелешь :(")

def spam():
    global users
    while True:
        for user in users:
            bot.send_message(user, "Затем сироп вишневый!")
        time.sleep(5)

def polling():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    thread = Thread(target=spam)
    thread.start()
    thread1 = Thread(target=polling)
    thread1.start()