from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

addWallet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '➕UZCARD'),
            KeyboardButton(text = '➕HUMO'),
            KeyboardButton(text = '➕QIWI')
        ],
        [
            KeyboardButton(text = '➕WMZ'),
            KeyboardButton(text = '➕WMR'),
            KeyboardButton(text = '➕PAYEER')
        ],
        [
            KeyboardButton(text = '➕Yandex'),
            KeyboardButton(text = '➕Сбербанк'),
            KeyboardButton(text = '➕Тинкофф')
        ],
        [
            KeyboardButton(text = '🔙Asosiy menyu')
        ]
    ], resize_keyboard=True, one_time_keyboard=True)