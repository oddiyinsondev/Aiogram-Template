from aiogram import types
from loader import dp
from states.Restran import Restran
from keyboards.default.menyu import menu




@dp.message_handler(text="🏘Boshsahifa")
async def Asosiy_sahifa(message: types.Message):
    await message.answer_photo(photo="https://i.ytimg.com/vi/ebDgFquhdXg/maxresdefault.jpg",caption = f"Asosiy menyuga Xush keldiz", reply_markup=menu)
    await Restran.menyu.set()



