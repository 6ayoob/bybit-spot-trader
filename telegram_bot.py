# telegram_bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_TOKEN
from trade_executor import positions

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_TELEGRAM_IDS:
        await update.message.reply_text("Unauthorized.")
        return
    await update.message.reply_text("🤖 بوت التداول جاهز.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "📊 الصفقات الحالية:\n"
    for symbol, price in positions.items():
        msg += f"- {symbol} @ {price}\n"
    if not positions:
        msg += "لا توجد صفقات حالياً."
    await update.message.reply_text(msg)

def run_telegram_bot():
    app = ApplicationBuilder().token("7800699278:AAEdMakvUEwysq-s0k9MsK6k4b4ucyHRfT4").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.run_polling()
