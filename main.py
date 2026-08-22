import telebot

TOKEN = "8906102424:AAHbjPTUHnAdqyancoB-QOg27gZx6vKGnKM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك! البوت يعمل الآن بنجاح على Render.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
