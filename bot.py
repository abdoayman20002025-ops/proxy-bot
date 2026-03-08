import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8696375934:AAE9NtOjgpiEJcylKihKEXYc9g8wfnw1yhA"

bot = telebot.TeleBot(TOKEN)

CHANNEL = "@elqanas2024"
ADMIN_ID = 6831561700
proxies = [

{"ip":"157.173.199.2","port":"7070","username":"qanas","password":"qanas"},{"ip":"162.245.238.81","port":"6868","username":"user646359706-1772991829","password":"9997e742b574"},
{"ip":"222.5.99","port":"3838","username":"user12287125144-1772991646","password":"a567ab4a3c18"},
{"ip":"5.221.133.39","port":"4479","username":"user12745686344-1772991646","password":"2ca567e31e18"},
{"ip":"5.127.93.60","port":"4569","username":"user12322848583-1772991646","password":"68c56fb75a"},
{"ip":"193.42.244.123","port":"2538","username":"user12127968284-1772991646","password":"e7b617bbcd"},
{"ip":"74.81.36.31","port":"8999","username":"user341992536-1772991646","password":"cb9d8f2d52"},
{"ip":"74.81.45.183","port":"2222","username":"user931283466-1772991646","password":"2d46a5a667"},
{"ip":"185.127.93.60","port":"4569","username":"user327161266-1772991646","password":"53d7b21b5f"},
{"ip":"74.81.35.2","port":"3339","username":"user12580282014-1772991646","password":"2d92f5596c"},
{"ip":"74.81.45.183","port":"2222","username":"user12901921344-1772991646","password":"6b5a15dc9b"},
{"ip":"147.124.205.248","port":"6999","username":"user420839945-1772991646","password":"2df533ae5a"},
{"ip":"74.81.40.205","port":"1159","username":"user824093306-1772991646","password":"206ce9b7e9"}

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


  SHORTLINK = "https://shrinkme.click/eY58"

users_opened_link = {}

@bot.message_handler(func=lambda m: m.text == "GET PROXY")
def send_proxy(message):

    user_id = message.from_user.id

    if user_id not in users_opened_link:
        users_opened_link[user_id] = False

    if not users_opened_link[user_id]:

        bot.send_message(
            message.chat.id,
            f"""
🔒 للحصول على البروكسي

افتح الرابط التالي أولاً 👇

{SHORTLINK}

بعد فتح الرابط ارجع واضغط GET PROXY مرة أخرى
"""
        )

        users_opened_link[user_id] = True
        return

    proxy = random.choice(proxies)

    text = f"""
IP: {proxy['ip']}
PORT: {proxy['port']}
USERNAME: {proxy['username']}
PASSWORD: {proxy['password']}
"""

    bot.send_message(message.chat.id, text)

    users_opened_link[user_id] = False    
bot.polling()



  
