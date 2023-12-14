from aiogram import types
from loader import dp, db
from states.Restran import Restran
from aiogram.dispatcher import FSMContext
from keyboards.default.menyu import menu
from keyboards.default.fast import Formmat


@dp.callback_query_handler(state=Restran.menyu)
async def sent_raqam(call: types.CallbackQuery, state: FSMContext):
    raqam_1 = int(call.data)
    await state.update_data(
        {"raqam_1": int(raqam_1)}
    )
    data = await state.get_data()
    taom = data.get("taom_1")
    n = data.get('narx')
    a = db.chek_product(tg_id=call.from_user.id, Product=taom)
    if db.chek_product(tg_id=call.from_user.id, Product=taom):
        k = int(raqam_1) + int(a[2])
        db.update_product(tg_id=call.from_user.id, Product=taom, quantity=k)
    else:
        db.add_product(call.from_user.id, taom, raqam_1)
    await call.message.answer(
        f"Siz ➡️ {taom} dan ➡️ {raqam_1} buyurdiz narxi: {Formmat(raqam_1 * n)} so'm\nKarzinkaga qo'shildi",
        reply_markup=menu)
    await state.finish()
