
import telebot
from telebot import types

TOKEN = "8728926232:AAEvG1mTmNbKRwgIdK9fRzrF6Bs8DUb2wMQ"
bot = telebot.TeleBot(TOKEN)

INSTA_LINK = "https://instagram.com/jasurbek__dcc"

# 🎬 6 ta kino
movies = {
    "1001": {"file_id": "BAACAgIAAxkBAAOwabeHbG_xsfiTezI7AAF939Dny6_BAAIlmwACuQa4SZ5oeWzOoROWOgQ", "name": "Kino 1"},
    "1002": {"file_id": "BAACAgIAAxkBAAOwabeHbG_xsfiTezI7AAF939Dny6_BAAIlmwACuQa4SZ5oeWzOoROWOgQ", "name": "Kino 2"},
    "1003": {"file_id": "BAACAgIAAxkBAAOrabdxF32qrNIVYefRYIsh0mlgTgEAArOaAAK5BrhJHOPQ4jUoNlQ6BA", "name": "Kino 3"},
    "1004": {"file_id": "BAACAgIAAxkBAAO3abeU9y3NaAVgpk2xtgABYw8965-hAAJ9mwACuQa4SfPlfGjSK7yJOgQ", "name": "Kino 4"},
    "1005": {"file_id": "BAACAgIAAxkBAAO1abePRql-bNBukxPhHtdlbQJZkgEAAkybAAK5BrhJE5drvobO3gM6BA", "name": "Kino 5"},
    "1006": {"file_id": "BAACAgIAAxkBAAOzabeI2U-kJt3R4qCeZL8HU1CbYDkAAiubAAK5BrhJLzafmV-zZxA6BA", "name": "Kino 6"},
}

# 🔘 Instagram tugma
def insta_button():
    markup = types.InlineKeyboardMarkup()
    
    btn1 = types.InlineKeyboardButton("📸 Instagramga kirish", url=INSTA_LINK)
    btn2 = types.InlineKeyboardButton("▶️ Davom etish", callback_data="continue")
    
    markup.add(btn1)
    markup.add(btn2)
    
    return markup

# 🔘 Menu
def menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📋 Kodlar", "🎬 Kino olish")
    return markup

# 🚀 START
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "❗ Iltimos Instagram sahifaga obuna bo‘ling:",
        reply_markup=insta_button()
    )

# ▶️ Davom etish
@bot.callback_query_handler(func=lambda call: call.data == "continue")
def continue_bot(call):
    bot.answer_callback_query(call.id, "✅ Davom eting")
    bot.send_message(call.message.chat.id, "Xush kelibsiz!", reply_markup=menu())

# 📋 Kodlar ro‘yxati
@bot.message_handler(func=lambda m: m.text == "📋 Kodlar")
def list_codes(msg):
    text = "📋 Kinolar:\n\n"
    for code, data in movies.items():
        text += f"{code} - {data['name']}\n"
    bot.send_message(msg.chat.id, text)

# 🎬 Kino yuborish
@bot.message_handler(func=lambda m: True)
def send_movie(msg):
    code = msg.text

    if code in movies:
        bot.send_video(
            msg.chat.id,
            movies[code]["file_id"],
            caption=movies[code]["name"]
        )
    else:
        bot.send_message(msg.chat.id, "❌ Kod topilmadi")

# 🔥 Doimiy ishlash
bot.infinity_polling(none_stop=True, interval=0, timeout=20)
