from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

royhat = ["Miniy HotDog", "Miniy Lavash", "Miniy Shoverma", "Miniy ChezBurger", "Obichniy HotDog", "Obichniy Lavash",
          "Obichniy Shoverma", "Obichniy ChezBurger"]
narx = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
fast_food = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
for roy in royhat:
    fast_food.insert(KeyboardButton(text=f"{roy}"))
fast_food.add(KeyboardButton(text="🔙 Orqaga"))


def narxchiq(taom: str) -> int:
    for i in range(0, len(royhat)):
        if royhat[i] == taom:
            return narx[i]
            break
    return 0


def Formmat(v: int):
    v_revers = str(v)[::-1]
    c = 0
    res = ""
    for i in v_revers:
        c += 1
        if c != 3:
            res += i
            c += 0
        else:
            c = 0
            res += i
            res += " "
    return res[::-1]
