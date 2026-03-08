import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8696375934:AAE9NtOjgpiEJcylKihKEXYc9g8wfnw1yhA"

bot = telebot.TeleBot(TOKEN)

CHANNEL = "@elqanas2024"
ADMIN_ID = 6831561700
proxies = [

{"ip":"157.173.199.2","port":"7070","username":"qanas","password":"qanas"}

]

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("GET PROXY"))


def check_sub(user_id):
    try:
        status = bot.get_chat_member(CHANNEL, user_id).status
        return status in ["member","administrator","creator"]
    except:
        return False


@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id
    args = message.text.split()

    if not check_sub(user_id):

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
            "📢 اشترك في قناة التليجرام",
            url="https://t.me/elqanas2024"
        )

        btn2 = InlineKeyboardButton(
            "▶ اشترك في قناة اليوتيوب",
            url="https://youtube.com/@albahth_3n_elmal"
        )

        btn3 = InlineKeyboardButton(
            "✅ تحقق من الاشتراك",
            callback_data="check"
        )

        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)

        bot.send_message(
            message.chat.id,
            "⚠️ يجب الاشتراك في القناة أولاً",
            reply_markup=markup
        )
        return


    bot.send_message(
        message.chat.id,
        "✅ مرحبًا بك في بوت البروكسي",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):

    if check_sub(call.from_user.id):

        bot.send_message(
            call.message.chat.id,
            "✅ تم التحقق من الاشتراك"
        )

    else:
        bot.answer_callback_query(call.id,"❌ لم تشترك في القناة بعد")


@bot.message_handler(func=lambda m: m.text == "GET PROXY")
def send_proxy(message):

    user_id = message.from_user.id

    proxy = random.choice(proxies)

    text = f"""
IP: {proxy['ip']}
PORT: {proxy['port']}
USERNAME: {proxy['username']}
PASSWORD: {proxy['password']}
"""

    bot.send_message(message.chat.id,text)
      
bot.polling()



  
