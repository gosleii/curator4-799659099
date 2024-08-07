import telebot
bot = telebot.TeleBot("7171002160:AAGWjH0hKOmKx0x8xPeti9W7UIA2MK57ipc")



@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "*Ассалямуалейкум!*", parse_mode="Markdown")

@bot.message_handler(commands=['history'])
def historyoftatarstan_handler(message):
    bot.send_message(message.chat.id, "Давай начнем знакомство с Татарстаном, посмотри видеоролик! [History of Tatarstan](https://youtu.be/KFSxLFipRbo?si=vQh5iNWN5wLcuq18)",)

@bot.message_handler(commands=['cities'])
def citiesoftatarstan_handler(message):
    bot.send_message(message.chat.id, "_Столица Татарстана - Казань\nГорода:\nАзнакаево\nАльметьевск\nБавлы\nБугульма\nБуинск\nЕлабуга\nЗаинск\nЗеленодольск\nКазань\nЛениногорск\nНабережные Челны\nНижнекамск\nНурлат\nЧистополь_", parse_mode="Markdown")

@bot.message_handler(commands=['population'])
def populationoftatarstan_handler(message):
    bot.send_message(message.chat.id, "Численность населения республики, по данным Росстата, составляет 4 003 016 человек", parse_mode="Markdown")


bot.infinity_polling()