def should_buy(symbol_data):
    return symbol_data.get("price", 0) < 1.0

def should_sell(symbol_data):
    return symbol_data.get("price", 0) > 2.0
