from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.main_menu import mainMenu
    

@dp.callback_query_handler(text = 'cancel', state = '*')
async def choose1(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Asosiy menyu', reply_markup = mainMenu)
    await call.message.delete()
    await state.finish()