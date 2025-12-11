import telebot
import qrcode
import random
from yt_dlp import YoutubeDL
from barcode import EAN13
from barcode.writer import ImageWriter

a = random.randint(1,10000)
b = random.randint(1,10000)

bot = telebot.TeleBot("8488594492:AAFqFtkDOVYeZGJObK-RKDmKwSAahvYz2t4")
# বটের দিকনির্দেশনা রিপ্লাই অংশ 
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,'আমাদের টেলিগ্রাম বটে আপনাকে স্বাগতম\nQR code জেনারেট করতে /qr লিখুন\nভিডিও ডাওনলোড করতে /dn লিখুন\বারকোড তৈরি করতে /brলিখুন ')
# QR code তৈরি করার ফাংশনালিটি 
@bot.message_handler(commands=['qr'])
def qr(message):
    bot.reply_to(message,'এখন আপনি যা লিখবেন তাই qrcode হিসেবে তৈরি হবে')
    bot.register_next_step_handler(message, qr_data)
def qr_data(message):
    filename = f"{a}_qr_data_{b}.png"
    img = qrcode.make(message.text)
    img.save(filename)
    bot.send_message(message.chat.id, f'qrcode তৈরি করা হয়েছে এই নামে "{filename}" এখন পাঠানো হবে ')
    bot.send_photo(message.chat.id, photo=open(filename,'rb'))
# বারকোড তৈরি করার ফাংশনালিটি 
@bot.message_handler(commands=['br'])
def br(message):
    bot.reply_to(message, 'বার কোড তৈরি করার জন্য কমপক্ষে ১৩ টি নাম্বার দিন, এবং এখন যা নাম্বার দিবেন সেটা তৈরি করা হবে')
    bot.register_next_step_handler(message, br_data)
def br_data(message):
    br_filename = f'{a}_brcode_{b}.png'
    code = EAN13(message.text, writer=ImageWriter())
    code.save(br_filename) 
    bot.send_message(message.chat.id,f'barcode তৈরি করা হয়েছে এই নামে "{br_filename}" এখন পাঠানো হবে )
    bot.send_photo(message.chat.id, photo=open(br_filename,'rb'))
#ভিডিও ডাওনলোড করার ফাংশনালিটি 
@bot.message_handler(commands=["dn"])
def dn(message):
    bot.reply_to(message,"আপনার ভিডিও এর লিংক দিন যেটা ডাওনলোড করতে চান")
    bot.register_next_step_handler(message, dn_data)
def dn_data(message):
    url = message.text
    video_name = f"{a}downloaded{b}.mp4"
    ops = {"outtmpl": video_name}
    with YoutubeDL(ops) as ydl:
        ydl.download([url])
    bot.send_message(message.chat.id,f'ভিডিও তৈরি হয়েছে {video_name} নামে, এখন পাঠানো হবে')
    bot.send_video(message.chat.id, open(video_name,"rb"))
print('bot is running')
bot.polling()




