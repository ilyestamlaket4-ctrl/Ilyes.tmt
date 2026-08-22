import os
import telebot
import google.generativeai as genai

# 1. إعداد المفاتيح (استبدل النصوص بين علامات التنصيص بمفاتيحك الخاصة)
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "ضع_توكن_تيليجرام_هنا")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "ضع_مفتاح_جيميناي_هنا")

# 2. تهيئة البوت ونموذج الذكاء الاصطناعي
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. معالجة أمر البداية /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "مرحباً بك! أنا بوت ذكاء اصطناعي جاهز للرد على جميع أسئلتك."
    bot.reply_to(message, welcome_text)

# 4. معالجة جميع الرسائل النصية وإرسالها لـ Gemini
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # إظهار مؤشر "جاري الكتابة..." في تيليجرام
        bot.send_chat_action(message.chat.id, 'typing')
        
        # توليد الرد من الذكاء الاصطناعي
        response = model.generate_content(message.text)
        
        if response.text:
            bot.reply_to(message, response.text)
        else:
            bot.reply_to(message, "عذراً، لم أستطع فهم الرسالة.")
            
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "حدث خطأ أثناء معالجة الطلب. يرجى التأكد من صحة المفاتيح.")

# 5. تشغيل البوت بشكل مستمر
if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
