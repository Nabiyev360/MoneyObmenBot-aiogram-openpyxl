from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp
from data.config import ADMINS
from keyboards.inline.chooselang import chooseLang
from utils.db_api.dbxl import add_user


@dp.message_handler(CommandStart(), state='*')      # Barcha state'larda ishlashi u-n state='*'
async def bot_start(message: types.Message, state: FSMContext):
    if message.text == '/start':            # If referral not aviable 
        await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\nВыберите язык / Tilni tanlang 💁‍♂️", reply_markup=chooseLang)
    else:                                    # If referral not aviable 
        referal_id = int(message.text[7:])          #/start so'zidan uyog'i referal nomeri
        try:
            await dp.bot.send_message(referal_id, f"{message.from_user.full_name} sizning havolangiz orqali botdan ro'yxatdan o'tdi")
        except:
            pass
    
    #USERNI RO'YXATGA OLISH
    add_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username)

    await dp.bot.send_message(ADMINS[0], 
    f"<a href='https://t.me/{message.from_user.username}'>{message.from_user.full_name}</a> start bosdi")
    
    await state.finish()