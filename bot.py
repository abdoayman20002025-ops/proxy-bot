import telebot
import random
import requests
import socket
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8696375934:AAFWdviaemoowA_sHyke9vBV5okUNuPj3Uc"

bot = telebot.TeleBot(TOKEN)

users = {}
all_users = set()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("GET PROXY"))


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

    bot.send_message(
        message.chat.id,
        "🔥 Welcome to Free Proxy Bot",
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda m: m.text == "GET PROXY")
def send_proxy(message):

    ip, port = get_proxy()

    if ip is None:

        bot.send_message(
            message.chat.id,
            "⚠️ No working proxy found try again"
        )

        return

    text = f"""
IP : {ip}
PORT : {port}
TYPE : SOCKS5
"""

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['users'])
def users_count(message):

    total = len(all_users)

    bot.send_message(
        message.chat.id,
        f"عدد مستخدمي البوت : {total}"
    )


bot.polling()
