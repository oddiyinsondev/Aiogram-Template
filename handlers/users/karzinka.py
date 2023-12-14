from aiogram import types
from loader import dp, db
from states.Restran import Restran
from aiogram.dispatcher import FSMContext
from keyboards.default.milliy import milliy
from keyboards.default.fast import fast_food
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default.menyu import menu
from keyboards.default.fast import Formmat
from keyboards.default.fast import narxchiq
import keyboards.default.milliy as narxchiq1


@dp.message_handler(text="🌭Fast food", state="*")
async def fast_fod(message: types.Message):
    await message.delete()
    await message.answer_photo(photo="https://i.pinimg.com/originals/2b/3f/ef/2b3fefd2c9b5873c17ce716d4917907e.jpg",
                               caption=f"Bizda hozircha shunday fast food taomlar mavjud", reply_markup=fast_food)
    await Restran.menyu.set()


@dp.message_handler(text="🥓Miliy taomlar", state="*")
async def fast_fod(message: types.Message):
    await message.delete()
    await message.answer_photo(photo="https://api.tourvillages.uz/media/images/restaurants/Gastronomic_tour_21.jpg",
                               caption=f"Bizda hozircha shunday milliy taomlar mavjud", reply_markup=milliy)
    await Restran.menyu.set()


@dp.message_handler(text="🗑Karzinka", state="*")
async def karzinka(message: types.Message):
    products = db.get_product(tg_id=message.from_user.id)
    msg = ""
    for product in products:
        if narxchiq(product[1]) != 0:
            msg += f"{product[1]} * {product[2]} dona narxi : {Formmat(narxchiq(product[1]) * product[2])} so'm\n"
        elif narxchiq1.narxchiq(product[1]) != 0:
            msg += f"{product[1]} * {product[2]} dona narxi : {Formmat(narxchiq1.narxchiq(product[1]) * product[2])} so'm\n"
    ochirish = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    for i in products:
        ochirish.insert(KeyboardButton(text=f"❌ {i[1]} ❌"))
    ochirish.add(KeyboardButton(text="🏘Boshsahifa"))
    if msg == "":
        msg = "Siz hech narsa xarid qilmadingiz."
    await message.answer(f"{msg}", reply_markup=ochirish)


@dp.message_handler(text_contains="❌ ", state="*")
async def ochirish_sned(message: types.Message, state: FSMContext):
    data = await state.get_data()
    taom = data.get("taom_1")
    raqam_1 = data.get("raqam_1")
    a = db.chek_product(tg_id=message.from_user.id, Product=taom)
    text = message.text
    text1 = text.replace("❌", "")
    text1 = text1.strip()
    if db.chek_product(tg_id=message.from_user.id, Product=text1):
        db.delete_product(tg_id=message.from_user.id, Product=text1)
        await message.answer(f"O'chirildi", reply_markup=menu)
    else:
        await message.answer("Malumot yoq")


@dp.message_handler(text="📜Bot haqida", state="*")
async def bot_haqida(message: types.Message):
    await message.delete()
    await message.answer("""
Bu botni biz sizga online\n
fast food hamda milliy taomlar\n
buyurtma berishingiz uchun yasadik
    """)
