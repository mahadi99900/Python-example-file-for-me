import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = " bot token "

DOWNLOAD_PATH = "/sdcard/Download"  # ভিডিও এখানে সেভ হবে

# 🔹 /start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 হাই! আমাকে যেকোনো ভিডিও লিংক পাঠাও, আমি তোমার জন্য ডাউনলোড করে দেব।")

# 🔹 ভিডিও লিংক পেলে
async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    await update.message.reply_text("📥 ভিডিও ডাউনলোড শুরু হচ্ছে, অনুগ্রহ করে অপেক্ষা করুন...")

    file_path = os.path.join(DOWNLOAD_PATH, "video.mp4")

    try:
        # 🔸 yt-dlp দিয়ে হাই কোয়ালিটিতে ডাউনলোড
        cmd = [
            "yt-dlp",
            "-f", "bestvideo+bestaudio/best",
            "-o", file_path,
            url
        ]
        subprocess.run(cmd, check=True)

        # 🔸 ডাউনলোড সম্পন্ন
        await update.message.reply_text("✅ ভিডিও সফলভাবে ডাউনলোড হয়েছে!\n📤 এখন তোমাকে পাঠানো হচ্ছে...")

        # 🔸 ফাইল পাঠানোর চেষ্টা
        with open(file_path, "rb") as video:
            await update.message.reply_video(video=video)

        await update.message.reply_text("🎉 ভিডিও পাঠানো সম্পন্ন!")

    except subprocess.CalledProcessError:
        await update.message.reply_text("❌ ভিডিও ডাউনলোডে সমস্যা হয়েছে, লিংকটি যাচাই করুন।")

    except Exception as e:
        # 🔸 ফাইল বড় বা পাঠানো সম্ভব নয়
        await update.message.reply_text(
            f"⚠️ ফাইলটি অনেক বড় বা Telegram এ পাঠানো যায়নি।\n📁 ভিডিওটি এখানে সংরক্ষণ করা হয়েছে:\n{file_path}"
        )

# 🔹 বট চালানো
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

    app.run_polling()

if __name__ == "__main__":
    main()