import os
import telebot
import google.generativeai as genai

# المفاتيح الخاصة بك
TELEGRAM_BOT_TOKEN = "8906102424:AAHbjPTUHnAdqyancoB-QOg27gZx6vKGnKM"
GEMINI_API_KEY = "AQ.Ab8RN6LJo5nyPk1i_zfomfYpIjucKz1KGZaaOu5Q1cIJpNOCRQ"

# تهيئة البوت ونموذج الذكاء الاصطناعي
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك! أنا بوت ذكاء اصطناعي جاهز للرد على جميع أسئلتك.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        response = model.generate_content(message.text)
        if response.text:
            bot.reply_to(message, response.text)
        else:
            bot.reply_to(message, "عذراً، لم أستطع فهم الرسالة.")
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "حدث خطأ أثناء معالجة الطلب.")

if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
