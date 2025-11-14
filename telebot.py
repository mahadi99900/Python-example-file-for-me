import telebot

BOT_TOKEN = "8488594492:AAFqFtkDOVYeZGJObK-RKDmKwSAahvYz2t4"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "হ্যালো! আমি বট, তুমি কি করতে চাও?")

@bot.message_handler(func=lambda message: True)
def echo(msg):
    bot.reply_to(msg, f"তুমি বলেছো: {msg.text}")

bot.polling()