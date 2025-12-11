import telebot

# টেলিগ্রাম বটের টোকেন
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# বট তৈরি করা
bot = telebot.TeleBot(TOKEN)

# /start কমাণ্ডের জন্য হ্যান্ডলার
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "হ্যালো, কেমন আছেন?")

# /help কমাণ্ডের জন্য হ্যান্ডলার
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "আপনি কি সাহায্য চান?")

# যে কোন মেসেজের জন্য হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "আপনি যা বলেছেন: " + message.text)

# বট চালু করা
bot.polling()