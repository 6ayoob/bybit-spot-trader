from pybit.unified_trading import HTTP

api_key = "YYYM7DuvzINADCosx"  # مفتاح API من Bybit
api_secret = "j3V4agrapGkQLSQsb75shiSWCTZe8t3TYnDdp"  # السر
session = HTTP(api_key=api_key, api_secret=api_secret)

def get_price(symbol="BTCUSDT"):
    data = session.get_tickers(category="spot", symbol=symbol)
    return float(data['result']['list'][0]['lastPrice'])

def place_order(symbol, side, usdt_amount):
    price = get_price(symbol)
    qty = round(usdt_amount / price, 6)
    order = session.place_order(
        category="spot",
        symbol=symbol,
        side=side,
        order_type="Market",
        qty=qty
    )
    print(f"✅ {side} {qty} {symbol}")
    return order

def get_balance():
    data = session.get_wallet_balance(accountType="UNIFIED")
    balance = float(data['result']['list'][0]['coin'][0]['walletBalance'])
    return round(balance, 2)
