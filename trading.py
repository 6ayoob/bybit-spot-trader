from pybit import HTTP
from config import *
import json

session = HTTP("https://api.bybit.com", api_key=YYYiM7DuvzINADCosx, api_secret=j3V4agrapGkqLSQsb75shiSWCTZe8a3TYnDdp)

def get_balance():
    wallet = session.get_wallet_balance(coin="USDT")
    return float(wallet['result']['USDT']['available_balance'])

def place_order(symbol, qty):
    return session.place_active_order(
        symbol=symbol,
        side="Buy",
        order_type="Market",
        qty=qty,
        time_in_force="GoodTillCancel"
    )

def calc_trade_amount(entry_price):
    balance = get_balance()
    amount_usdt = balance * RISK_PER_TRADE
    qty = round(amount_usdt / entry_price, 3)
    return qty

def save_position(symbol, entry, tp, sl):
    with open("positions.json", "r+") as f:
        data = json.load(f)
        data[symbol] = {"entry": entry, "tp": tp, "sl": sl}
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()
