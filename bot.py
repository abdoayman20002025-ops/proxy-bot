import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8696375934:AAE9NtOjgpiEJcylKihKEXYc9g8wfnw1yhA"

bot = telebot.TeleBot(TOKEN)

CHANNEL = "@elqanas2024"

proxies = [

{
"ip":"74.81.45.135",
"port":"1258",
"username":"user12943686834-1772906369",
"password":"66894b94d6"
}
,
{
    "ip":"45.32.204.208",
    "port":"16118",
    "username":"ghost",
    "password":"ghost"
}
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

    if not check_sub(message.from_user.id):

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
            "⚠️ لازم تشترك في القناة عشان تستخدم البوت",
            reply_markup=markup
        )
        return

    bot.send_message(
        message.chat.id,
        "اهلا بك في بوت البروكسي",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):

    if check_sub(call.from_user.id):

        bot.send_message(
            call.message.chat.id,
            "✅ تم التحقق يمكنك الآن استخدام البوت",
            reply_markup=keyboard
        )

    else:
        bot.answer_callback_query(call.id,"❌ لم تشترك في القناة بعد")


@bot.message_handler(func=lambda m: m.text == "GET PROXY")
def send_proxy(message):

    proxy = random.choice(proxies)

    text = f"""
IP: {proxy['ip']}
PORT: {proxy['port']}
USERNAME: {proxy['username']}
PASSWORD: {proxy['password']}
"""

    bot.send_message(message.chat.id, text)



bot.polling()


