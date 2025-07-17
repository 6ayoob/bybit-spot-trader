from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import *
from trading import *
from utils import format_trade

def start(update: Update, context: CallbackContext):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    update.message.reply_text("✅ البوت يعمل بنجاح!")

def scan(update: Update, context: CallbackContext):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    for symbol in TRADE_SYMBOLS:
        price = session.latest_information_for_symbol(symbol=symbol)['result'][0]['last_price']
        price = float(price)
        qty = calc_trade_amount(price)
        order = place_order(symbol, qty)
        tp = round(price * (1 + TAKE_PROFIT_PERCENT/100), 4)
        sl = round(price * (1 - STOP_LOSS_PERCENT/100), 4)
        save_position(symbol, price, tp, sl)
        msg = format_trade(symbol, price, tp, sl)
        update.message.reply_text(msg)

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("scan", scan))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()