from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

clearWallets = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = "♨️Tozalash", callback_data = "clear_wallets")   
        ]
    ]
)