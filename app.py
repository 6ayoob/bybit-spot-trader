# app.py
import time
import threading
from config import SYMBOLS
from strategies import should_buy
from trade_executor import buy, manage_positions
from telegram_bot import run_telegram_bot
from pybit.unified_trading import HTTP
from utils import log

session = HTTP()

def fetch_price(symbol):
    tick = session.get_ticker(category="spot", symbol=symbol)
    return float(tick["result"][0]["lastPrice"])

def fetch_ma(symbol, period):
    klines = session.get_kline(category="spot", symbol=symbol, interval="60", limit=period)
    closes = [float(k[4]) for k in klines["result"]["list"]]
    return sum(closes) / len(closes)

def main_loop():
    while True:
        prices = {}
        for symbol in SYMBOLS:
            try:
                price = fetch_price(symbol)
                ma50 = fetch_ma(symbol, 50)
                ma200 = fetch_ma(symbol, 200)
                prices[symbol] = price

                if should_buy(price, ma50, ma200):
                    buy(symbol, price)

            except Exception as e:
                log(f"خطأ في {symbol}: {e}")
        manage_positions(prices)
        time.sleep(1800)  # كل 30 دقيقة

# تشغيل التليجرام والبوت معًا
threading.Thread(target=run_telegram_bot).start()
main_loop()
