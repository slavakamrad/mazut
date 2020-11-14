import telebot

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
        bot.send_message(message.chat.id, "Уже уходишь, {}? Я буду скучать -(".format(username))
    elif message.text == "Сосешь?":
        bot.send_message(message.chat.id, "Хуй сосет Байден и негры. А я тока спирт потягиваю.")
    #else:
    #    bot.send_message(message.chat.id, "Я еще слишком глуп, и не знаю что ответить...")


bot.polling()
