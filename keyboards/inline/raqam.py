from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

raqamlar = InlineKeyboardMarkup(row_width=3)
for roy in range(1, 10):
    a = InlineKeyboardButton(text=str(roy), callback_data=str(roy))
    raqamlar.insert(a)
