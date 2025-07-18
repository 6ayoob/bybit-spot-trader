positions = {}

def get_positions():
    return positions

def open_position(symbol, data):
    positions[symbol] = data

def close_position(symbol):
    if symbol in positions:
        del positions[symbol]
