from aiogram.types import CallbackQuery

from loader import dp
from utils.db_api.dbxl import check_trans

@dp.callback_query_handler(text = "trans_success", state="*")
async def status1(call: CallbackQuery):
    trans_id = call.message.text[13:16]    
    TEXT = f"ID: {trans_id}\n✅Sizning almashuvingiz <b>Muvaffaqiyatli</b> yakunlandi\n"
    
    try:
        await dp.bot.send_message(chat_id = check_trans(trans_id, 'successful'), text = TEXT)
    except:
        pass
    await call.message.delete()


@dp.callback_query_handler(text = "trans_fail", state="*")
async def status2(call: CallbackQuery):
    trans_id = call.message.text[13:16]
    TEXT = f"ID: {trans_id}\n❌Sizning so'rovingiz <b>Rad etildi!</b>\nSiz berilgan raqamga to'lov qilmagansiz"
    
    try:
        await dp.bot.send_message(chat_id = check_trans(trans_id, 'cancelled'), text = TEXT)
    except:
        pass
    await call.message.delete()