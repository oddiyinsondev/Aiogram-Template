from aiogram import types
from loader import dp
from states.Restran import Restran
from aiogram.dispatcher import FSMContext
from keyboards.default.milliy import royhat1
from keyboards.default.fast import royhat
from keyboards.inline.raqam import raqamlar
from keyboards.default.menyu import menu
from keyboards.default.fast import Formmat
from keyboards.default.fast import narxchiq
import keyboards.default.milliy as naxchiq1


@dp.message_handler(state=Restran.menyu)
async def taomlar(message: types.Message, state: FSMContext):
    taom_1 = message.text
    await state.update_data(
        {"taom_1": taom_1}
    )
    qator1 = royhat
    qator2 = royhat1
    if taom_1 in qator1:
        await message.answer_photo(
            photo="https://avatars.mds.yandex.net/i?id=b57c6d44c3b622678d03c845dab523a75588a95f-9829492-images-thumbs&n=13",
            caption=f"Nechta buyurtma bermoqchisiz narxi: {Formmat(narxchiq(taom_1))} so'm", reply_markup=raqamlar)
        await state.update_data({"narx": narxchiq(taom_1)})
    elif taom_1 in qator2:
        await message.answer_photo(
            photo="https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663790596_14-mykaleidoscope-ru-p-uzbekskie-frukti-yeda-oboi-16.jpg",
            caption=f"Nechta buyurtma bermoqchisiz narxi: {Formmat(naxchiq1.narxchiq(taom_1))} so'm",
            reply_markup=raqamlar)
        await state.update_data({"narx": naxchiq1.narxchiq(taom_1)})
    else:
        await message.answer_photo(photo="https://i.ytimg.com/vi/ebDgFquhdXg/maxresdefault.jpg",
                                   caption=f"Asosiy menyuga Xush keldiz", reply_markup=menu)
        await Restran.menyu.set()
