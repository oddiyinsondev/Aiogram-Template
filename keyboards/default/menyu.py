from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

royhat = ["🌭Fast food", "🥓Miliy taomlar", "🗑Karzinka", "📜Bot haqida"]

menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for roy in royhat:
    menu.insert(KeyboardButton(text=f"{roy}"))
    