import telebot
import time
from bybit_client import place_order, get_balance, get_price
from strategies import should_buy, should_sell

BOT_TOKEN = '7800699278:AAEdMakvUEwysq-s0k9MsK6k4b4ucyHRfT4'
bot = telebot.TeleBot(BOT_TOKEN)

ALLOWED_USERS = [7863509137]  # عدل هذا بمعرفك إن أردت
SYMBOL = "BTCUSDT"
TRADE_QTY = 10  # الكمية بالدولار

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id in ALLOWED_USERS:
        bot.reply_to(message, "🤖 تم تشغيل بوت التداول الآلي لـ Bybit.")

@bot.message_handler(commands=['balance'])
def balance(message):
    if message.from_user.id in ALLOWED_USERS:
        bal = get_balance()
        bot.reply_to(message, f"💰 رصيدك: {bal} USDT")

def auto_trade():
    while True:
        price = get_price(SYMBOL)
        if should_buy(price):
            place_order(SYMBOL, "Buy", TRADE_QTY)
        elif should_sell(price):
            place_order(SYMBOL, "Sell", TRADE_QTY)
        time.sleep(60)  # كل دقيقة

import threading
threading.Thread(target=auto_trade).start()

bot.infinity_polling()
