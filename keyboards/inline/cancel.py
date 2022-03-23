from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Cancel = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = f"Bekor qilish ❌", callback_data='cancel')
        ],
])