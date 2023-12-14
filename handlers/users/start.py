import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.Restran import Restran
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.menyu import menu


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer_photo(photo="https://i.ytimg.com/vi/ebDgFquhdXg/maxresdefault.jpg",caption = f"Xush kelibsiz! {name}", reply_markup=menu)
        await Restran.menyu.set()
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer_photo(photo="https://i.ytimg.com/vi/ebDgFquhdXg/maxresdefault.jpg",caption = f"Xush kelibsiz! {name}", reply_markup=menu)
        await Restran.menyu.set()