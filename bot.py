from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8714894439:AAHv4XZ4uxcwmp4LKj_6I6CEx_Do_owNNzA"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "salom":
        await update.message.reply_text("Alik 👋")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()
