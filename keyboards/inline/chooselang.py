from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

chooseLang = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text ="O'zbek tili ๐บ๐ฟ", callback_data = 'UZ')
        ],
        [
            InlineKeyboardButton(text = "ะ ัััะบะธะน ๐ท๐บ", callback_data = 'RU'),
            InlineKeyboardButton(text = "English ๐ฌ๐ง", callback_data = 'ENG')
        ],
])