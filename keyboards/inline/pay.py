from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

payOrCancel = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text ="To'lov qilish", callback_data = 'pay')
        ],
        [
            InlineKeyboardButton(text = "Bekor qilish ❌", callback_data = 'cancel'),
        ],
])

payedOrCancel = InlineKeyboardMarkup(
        inline_keyboard = [
        [
            InlineKeyboardButton(text ="To'lov qildim ✅", callback_data = 'payed')
        ],
        [
            InlineKeyboardButton(text = "Bekor qilish ❌", callback_data = 'cancel'),
        ],
])