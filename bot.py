import telebot
from get_fin_quotes import *
from tiker_list import tiker_list
from get_fin_news import *
from get_rus_qoutes import *

TOKEN = '1327008721:AAF8QJUstDeetV3XIcmgsIdBjEx2TBst4ZQ'
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
    elif message.text == "новости":
        bot.send_message(message.chat.id, post_news())
    elif message.text == "RUS":
        def get_tiker(message):
            try:
                bot.send_message(message.chat.id, get_ru_quotes(str(message.text)))
                print(message.text, "ХУЙ", get_ru_quotes(str(message.text)))
            except RuntimeError:
                stock_except()
        msg = bot.send_message(message.chat.id, "Введите тикер: ")

        bot.register_next_step_handler(msg, get_tiker)

bot.polling()