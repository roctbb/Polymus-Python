import telebot
from threading import Thread

import time

token = "YOUR TOKEN"

bot = telebot.TeleBot(token)

users = set()

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