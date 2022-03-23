from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

chooseLang = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text ="O'zbek tili 🇺🇿", callback_data = 'UZ')
        ],
        [
            InlineKeyboardButton(text = "Русский 🇷🇺", callback_data = 'RU'),
            InlineKeyboardButton(text = "English 🇬🇧", callback_data = 'ENG')
        ],
])