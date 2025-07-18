import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from trade_executor import get_positions

BOT_TOKEN = "7800699278:AAEdMakvUEwysq-s0k9MsK6k4b4ucyHRfT4"
ALLOWED_USERS = [658712542]

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USERS:
        return await update.message.reply_text("🚫 غير مصرح لك باستخدام هذا البوت.")
    await update.message.reply_text("🤖 بوت التداول يعمل!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ALLOWED_USERS:
        return await update.message.reply_text("🚫 غير مصرح لك باستخدام هذا البوت.")
    positions = get_positions()
    if not positions:
        await update.message.reply_text("لا توجد صفقات مفتوحة حاليًا.")
    else:
        msg = "\n".join([f"{symbol}: {info}" for symbol, info in positions.items()])
        await update.message.reply_text(f"📊 الصفقات المفتوحة:\n{msg}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))

if __name__ == "__main__":
    app.run_polling()
