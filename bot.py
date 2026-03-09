import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8696375934:AAFWdviaemoowA_sHyke9vBV5okUNuPj3Uc"

bot = telebot.TeleBot(TOKEN)

CHANNEL = "@elqanas2024"

SHORTLINK = "https://shrinkme.click/eY58"

users = {}
all_users = set()

proxies = [

{"ip":"162.245.238.81","port":"6868","username":"user646359706","password":"9997e742b574"},

{"ip":"222.5.99.2","port":"3838","username":"user12287125144","password":"a567ab4a3c18"},

{"ip":"5.221.133.39","port":"4479","username":"user12745686344","password":"2ca567e31e18"},

{"ip":"185.127.93.60","port":"4569","username":"user12322848583","password":"68c56fb75a19"},

{"ip":"193.42.244.123","port":"2538","username":"user12127968284","password":"e7b617bbcd"}

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
    all_users.add(user_id)

    if not check_sub(user_id):

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
        "اشترك في القناة",
        url="https://t.me/elqanas2024"
        )

        btn2 = InlineKeyboardButton(
        "تحقق من الاشتراك",
        callback_data="check"
        )

        markup.add(btn1)
        markup.add(btn2)

        bot.send_message(
        message.chat.id,
        "لازم تشترك في القناة عشان تستخدم البوت",
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
        "تم التحقق يمكنك استخدام البوت",
        reply_markup=keyboard
        )

    else:

        bot.answer_callback_query(
        call.id,
        "لم تشترك في القناة بعد"
        )


@bot.message_handler(func=lambda m: m.text == "GET PROXY")
def send_proxy(message):

    user_id = message.from_user.id

    markup = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton("افتح الرابط", url=SHORTLINK)
    btn2 = InlineKeyboardButton("تحقق", callback_data="verify")

    markup.add(btn1)
    markup.add(btn2)

    users[user_id] = True

    bot.send_message(
    message.chat.id,
    "افتح الرابط ثم اضغط تحقق للحصول على البروكسي",
    reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "verify")
def verify(call):

    user_id = call.from_user.id

    if user_id not in users:

        bot.answer_callback_query(call.id,"افتح الرابط أولا")
        return

    proxy = random.choice(proxies)

    text = f"""
IP : {proxy['ip']}
PORT : {proxy['port']}
USERNAME : {proxy['username']}
PASSWORD : {proxy['password']}
"""

    bot.send_message(call.message.chat.id, text)

    users.pop(user_id)


@bot.message_handler(commands=['users'])
def users_count(message):

    total = len(all_users)

    bot.send_message(
    message.chat.id,
    f"عدد مستخدمي البوت : {total}"
    )


bot.polling()
