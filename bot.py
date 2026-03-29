from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8402178729:AAHAJiUKS1IhB1uzJRMgfyhj5MAKOKZX-7s"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "salom":
        await update.message.reply_text("Alik 👋")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()
