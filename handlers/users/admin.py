from aiogram.types import Message 

from loader import dp
from data.config import ADMINS

@dp.message_handler(user_id = ADMINS[0], text = ['getdb', 'transfers'])
async def admin(message: Message):
    if message.text == 'getdb':
        file = open('database.xlsx', 'rb')
        await message.answer_document(file)
        file.close()
    
    elif message.text == 'transfers':
        file = open('transfers.xlsx', 'rb')
        await message.answer_document(file)
        file.close()


@dp.message_handler(user_id = ADMINS[0], content_types=['document'])
async def admin_file(message: Message):
    file_name = message.document.file_name      # "database.xlsx"
    if file_name in ['database.xlsx', 'transfers.xlsx']:
        file_id = message.document.file_id      # BQACAgIAAxkBAAIi52GVb3sH3MgKej887YiXt52gLmk_AAKyDgACMWixSHQ0T8RJZQAB-SIE
        file = await dp.bot.get_file(file_id)   # {"file_id": "BQACAgIAAxkBAAIi52GVb3sH3MgKej887YiXt52gLmk_AAKyDgACMWixSHQ0T8RJZQAB-SIE", "file_unique_id": "AgADsg4AAjFosUg", "file_size": 1462, "file_path": "documents/file_13.ppk"}
        file_path = file.file_path              # documents/file_13.xlsx
        
        await dp.bot.download_file(file_path, file_name)