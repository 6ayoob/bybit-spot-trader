# strategies.py
def should_buy(latest_price, ma_50, ma_200):
    return ma_50 > ma_200 and latest_price > ma_50

def should_sell(latest_price, buy_price, take_profit_pct, stop_loss_pct):
    profit_target = buy_price * (1 + take_profit_pct / 100)
    stop_loss = buy_price * (1 - stop_loss_pct / 100)
    if latest_price >= profit_target:
        return "take_profit"
    elif latest_price <= stop_loss:
        return "stop_loss"
    return None
