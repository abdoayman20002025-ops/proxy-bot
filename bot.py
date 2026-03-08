import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8696375934:AAE9NtOjgpiEJcylKihKEXYc9g8wfnw1yhA"

bot = telebot.TeleBot(TOKEN)

CHANNEL = "@elqanas2024"
REQUIRED_INVITES = 3

users = {}
invites = {}

proxies = [

{"ip":"89.167.56.176","port":"30289","username":"rtgxkhe3iu","password":"dKJrZPhesQ"}

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

    if user_id not in invites:
        invites[user_id] = 0

    if len(args) > 1:
        ref = int(args[1])

        if ref != user_id:

            if ref not in users:
                users[ref] = []

            if user_id not in users[ref]:
                users[ref].append(user_id)

                if ref not in invites:
                    invites[ref] = 0

                invites[ref] += 1


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


    if invites[user_id] < REQUIRED_INVITES:

        bot.send_message(
            message.chat.id,
            f"""
🚫 يجب دعوة {REQUIRED_INVITES} أصدقاء لاستخدام البوت

عدد دعواتك: {invites[user_id]}

رابط الدعوة الخاص بك:
https://t.me/{bot.get_me().username}?start={user_id}
"""
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

    if invites.get(user_id,0) < REQUIRED_INVITES:

        bot.send_message(
            message.chat.id,
            "🚫 يجب دعوة 3 أشخاص أولاً"
        )
        return

    proxy = random.choice(proxies)

    text = f"""
IP: {proxy['ip']}
PORT: {proxy['port']}
USERNAME: {proxy['username']}
PASSWORD: {proxy['password']}
"""

    bot.send_message(message.chat.id,text)


bot.polling()
