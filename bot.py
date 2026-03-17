import telebot
import random
import requests
import socket
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8696375934:AAFWdviaemoowA_sHyke9vBV5okUNuPj3Uc"

bot = telebot.TeleBot(TOKEN)

CHANNEL = "@elqanas2024"
YOUTUBE = "https://youtube.com/@albahth_3n_elmal"
SHORTLINK = "https://shrinkme.click/eY58"

users = {}
all_users = set()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("GET PROXY"))


def check_sub(user_id):
    try:
        status = bot.get_chat_member(CHANNEL, user_id).status
        return status in ["member","administrator","creator"]
    except:
        return False


def proxy_sources():
    return [
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt"
    ]


def check_proxy(ip, port):
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((ip, int(port)))
        s.close()
        return True
    except:
        return False


def get_proxy():
    proxy_list = []

    for url in proxy_sources():
        try:
            r = requests.get(url, timeout=10)
            proxy_list += r.text.splitlines()
        except:
            pass

    random.shuffle(proxy_list)

    for proxy in proxy_list:
        try:
            ip, port = proxy.split(":")
            if check_proxy(ip, port):
                return ip, port
        except:
            pass

    return None, None


@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id
    all_users.add(user_id)

    if not check_sub(user_id):

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
        "اشترك في التليجرام",
        url="https://t.me/elqanas2024"
        )

        btn2 = InlineKeyboardButton(
        "اشترك في اليوتيوب",
        url=YOUTUBE
        )

        btn3 = InlineKeyboardButton(
        "تحقق من الاشتراك",
        callback_data="check_sub"
        )

        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)

        bot.send_message(
        message.chat.id,
        "⚠️ لازم تشترك في القناة واليوتيوب الأول",
        reply_markup=markup
        )

        return

    bot.send_message(
    message.chat.id,
    "🔥 اهلا بك في بوت البروكسي",
    reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_subscription(call):

    if check_sub(call.from_user.id):

        bot.send_message(
        call.message.chat.id,
        "✅ تم التحقق تقدر تستخدم البوت",
        reply_markup=keyboard
        )

    else:

        bot.answer_callback_query(
        call.id,
        "❌ لازم تشترك الأول"
        )


@bot.message_handler(func=lambda m: m.text == "GET PROXY")
def send_proxy(message):

    user_id = message.from_user.id

    # لازم يدخل اللينك الأول
    if users.get(user_id, False) == False:

        users[user_id] = True

        bot.send_message(
        message.chat.id,
        f"""🔒 للحصول على البروكسي

افتح الرابط ده الأول 👇
{SHORTLINK}

وبعدين اضغط GET PROXY تاني"""
        )

        return

    ip, port = get_proxy()

    if ip is None:

        bot.send_message(
        message.chat.id,
        "⚠️ مفيش بروكسي شغال دلوقتي جرب تاني"
        )

        return

    text = f"""
IP : {ip}
PORT : {port}
TYPE : SOCKS5
"""

    bot.send_message(message.chat.id, text)

    users[user_id] = False


@bot.message_handler(commands=['users'])
def users_count(message):

    total = len(all_users)

    bot.send_message(
    message.chat.id,
    f"👥 عدد المستخدمين: {total}"
    )


bot.polling()
