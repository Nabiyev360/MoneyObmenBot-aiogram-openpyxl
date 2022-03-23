from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def givOrTake(berish, olish):
    choose_type = InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(text = f"Berishni kiritish * {berish}", callback_data = "choosen_berish")
            ],
            [
                InlineKeyboardButton(text = f"Olishni kiritish * {olish}", callback_data = "choosen_olish")
            ],
            [
                InlineKeyboardButton(text = f"🚫 Bekor qilish", callback_data='cancel')
            ]
        ]
        )
    return choose_type