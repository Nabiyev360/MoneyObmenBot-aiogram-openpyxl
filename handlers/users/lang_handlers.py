from aiogram.types import CallbackQuery
from keyboards.default.main_menu import mainMenu
from loader import dp

@dp.callback_query_handler(text = 'UZ')
async def choose_language(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Asosiy menyu", reply_markup = mainMenu)

@dp.callback_query_handler(text = 'RU')
async def choose_language(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Главный меню", reply_markup = mainMenu)

@dp.callback_query_handler(text = 'ENG')
async def choose_language(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Main menu", reply_markup = mainMenu)