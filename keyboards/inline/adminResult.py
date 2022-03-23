from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


success_or_fail = InlineKeyboardMarkup(
        inline_keyboard = [
        [
            InlineKeyboardButton(text ="✅Muvaffaqiyatli", callback_data = 'trans_success')
        ],
        [
            InlineKeyboardButton(text = "❌Bekor qilish", callback_data = 'trans_fail'),
        ],
])