import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8696375934:AAE9NtOjgpiEJcylKihKEXYc9g8wfnw1yhA"

bot = telebot.TeleBot(TOKEN)

# هنا تضيف البروكسيات
proxies = [

{
"ip":"89.167.56.176",
"port":"30289",
"username":"rtgxkhe3iu",
"password":"dKJrZPhesQ"
}

]

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("GET PROXY"))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Welcome to Proxy Bot",
        reply_markup=keyboard
    )

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
