import telebot
from get_fin_quotes import *
from tiker_list import tiker_list

TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    print("Бомж начал работу")
    bot.send_message(message.chat.id, "Бомж активирован и готов к работе")


@bot.message_handler(content_types=['text'])
def send_text(message):

    print("Получено новое сообщение:", message.text)
    username = message.from_user.first_name
    if message.text == "Привет":
        bot.send_message(message.chat.id,
                         "{}, 🤝 Добро пожаловать в чат ".format(username))
    elif message.text == "Пока":
        bot.send_message(message.chat.id, "Уже уходишь, {}? Акции сами себя не купят".format(username))
    elif message.text in tiker_list:
        bot.send_message(message.chat.id, get_fin_quotes(message.text))
    elif message.text == "евро":
        bot.send_message(message.chat.id, exchange_rate_euro())
    elif message.text == "доллар":
        bot.send_message(message.chat.id, exchange_rate_usd())
bot.polling()
