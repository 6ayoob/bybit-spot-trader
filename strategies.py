# استراتيجية بسيطة: الشراء إذا السعر أقل من 61 ألف، البيع إذا فوق 64 ألف

def should_buy(price):
    return price < 61000

def should_sell(price):
    return price > 64000
