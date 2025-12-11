import telebot

# টেলিগ্রাম বটের টোকেন
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# বট তৈরি করা
bot = telebot.TeleBot(TOKEN)

# /start কমাণ্ডের জন্য হ্যান্ডলার
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "হ্যালো! আমি বাংলাদেশ সম্পর্কে তথ্য দিতে পারি।")

# বাংলাদেশের রাজধানী সম্পর্কে তথ্য
@bot.message_handler(commands=['রাজধানী'])
def capital(message):
    bot.reply_to(message, "বাংলাদেশের রাজধানী ঢাকা।")

# বাংলাদেশের আয়তন সম্পর্কে তথ্য
@bot.message_handler(commands=['আয়তন'])
def area(message):
    bot.reply_to(message, "বাংলাদেশের আয়তন ১,৪৭,৫৭০ বর্গ কিলোমিটার।")

# বাংলাদেশের জনসংখ্যা সম্পর্কে তথ্য
@bot.message_handler(commands=['জনসংখ্যা'])
def population(message):
    bot.reply_to(message, "বাংলাদেশের জনসংখ্যা প্রায় ১৬ কোটি।")

# বাংলাদেশের ভাষা সম্পর্কে তথ্য
@bot.message_handler(commands=['ভাষা'])
def language(message):
    bot.reply_to(message, "বাংলাদেশের রাষ্ট্রভাষা বাংলা।")

# যে কোন প্রশ্নের উত্তর দেওয়ার জন্য হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def echo(message):
    if 'কেমন আছো' in message.text:
        bot.reply_to(message, "আলহামদুলিল্লাহ, ভালো আছি।")
    elif 'বাংলাদেশের রাজধানী কি' in message.text:
        bot.reply_to(message, "বাংলাদেশের রাজধানী ঢাকা।")
    else:
        bot.reply_to(message, "আপনার প্রশ্নের উত্তর জানি না।")

# বট চালু করা
bot.polling()