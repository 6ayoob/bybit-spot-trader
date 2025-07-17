# trade_executor.py
from pybit.unified_trading import HTTP
from config import API_KEY, API_SECRET, RISK_PER_TRADE, TAKE_PROFIT_PERCENT, STOP_LOSS_PERCENT
from strategies import should_sell
from utils import log

session = HTTP(api_key=API_KEY, api_secret=API_SECRET)

positions = {}

def buy(symbol, price):
    usdt_qty = TRADE_AMOUNT / price
    session.place_order(category="spot", symbol=symbol, side="Buy", order_type="Market", qty=usdt_qty)
    positions[symbol] = price
    log(f"تم شراء {symbol} بسعر {price}")

def sell(symbol, price):
    usdt_qty = TRADE_AMOUNT / price
    session.place_order(category="spot", symbol=symbol, side="Sell", order_type="Market", qty=usdt_qty)
    positions.pop(symbol, None)
    log(f"تم بيع {symbol} بسعر {price}")

def manage_positions(current_prices):
    for symbol, buy_price in positions.items():
        current = current_prices[symbol]
        action = should_sell(current, buy_price, TAKE_PROFIT_PERCENT, STOP_LOSS_PERCENT)
        if action:
            sell(symbol, current)
