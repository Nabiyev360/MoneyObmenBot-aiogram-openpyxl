from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '♻️ Valyuta ayirboshlash')
        ],
        [
            KeyboardButton(text = '🗂Hamyonlar'),
            KeyboardButton(text = '📈Kurs | Zahira')
        ],
        [
            KeyboardButton(text = '🔁Almashinuvlar'),
            KeyboardButton(text = 'ℹ️Ma\'lumotlar')
        ],
        [
            KeyboardButton(text = '🍋QIWI identifikatsiya')
        ],
        [
            KeyboardButton(text = '👥Referallar'),
            KeyboardButton(text = '👨🏻‍💻Aloqa')
        ]  
    ], one_time_keyboard=True)