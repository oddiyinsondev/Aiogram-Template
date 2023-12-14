from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

royhat1 = ["Obichni Osh", "Obichni Barak", "Obichni Shorva", "Obichni Shashlik", "Kok Barak", "Obichni Tuxum Barak"]
narx = [25000, 26000, 27000, 28000, 29000, 30000]
milliy = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
for roy in royhat1:
    milliy.insert(KeyboardButton(text=f"{roy}"))
milliy.add(KeyboardButton(text="🔙 Orqaga"))


def narxchiq(taom: str) -> int:
    for i in range(0, len(royhat1)):
        if royhat1[i] == taom:
            return narx[i]
            break
    return 0
