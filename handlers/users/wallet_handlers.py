from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from utils.db_api.dbxl import addWallet_db, clearWallets
from keyboards.default.main_menu import mainMenu
from keyboards.default.wallet_keyboard import addWallet
from states.mapMenu import Map
from states.mapWallet import EditWallet


@dp.message_handler(text = '🔙Asosiy menyu', state = "*")   # Asosiy menuga qaytish
async def change(message: types.Message, state:FSMContext):
    await message.answer('Asosiy menyu', reply_markup=mainMenu)
    await state.finish()

@dp.message_handler(text = ['➕UZCARD', '➕HUMO', '➕QIWI', '➕WMZ', '➕WMR', '➕Yandex', '➕PAYEER', '➕Тинкофф', '➕Сбербанк'], state = "*")
async def change(message: types.Message, state:FSMContext):
    retext = " raqamlarini kiriting.\nBo'sh joylarsiz, boshqa belgilarsiz"
    if message.text == '➕UZCARD':
        text = 'UZCARD kartangiz'+retext
        await EditWallet.EditUzcard.set()
    
    elif message.text == '➕HUMO':
        text = 'HUMO kartangiz'+retext
        await EditWallet.EditHumo.set()
        
    elif message.text == '➕QIWI':
        text = 'QIWI hamyoningiz raqamini kiriting.\n\nFormat: +998901234567'
        await EditWallet.EditQiwi.set()
        
    elif message.text == '➕WMZ':
        text = 'WMZ hisobingiz' + retext + "\n\nFormat: Z123456789012"
        await EditWallet.EditWMZ.set()
        
    elif message.text == '➕WMR':
        text = 'WMR hisobingiz' + retext + "\n\nFormat: R123456789012"
        await EditWallet.EditWMR.set()
        
    elif message.text == '➕Yandex':
        text = 'Yandex hisobingiz'+retext
        await EditWallet.EditYandex.set()
        
    elif message.text == '➕PAYEER':
        text = 'PAYEER hisobingiz'+retext
        await EditWallet.EditPayeer.set()
        
    elif message.text == '➕Тинкофф':
        text = 'Тинкофф hisobingiz'+retext
        await EditWallet.EditTinkoff.set()
        
    elif message.text == '➕Сбербанк':
        text = 'Сбербанк hisobingiz'+retext
        await EditWallet.EditSberbank.set()
    
    await message.reply(text)


# Add UZCARD
@dp.message_handler(state = EditWallet.EditUzcard)
async def change(message: types.Message, state:FSMContext):
    card_num = message.text
    
    try:
        card_num = int(card_num)   
    except:
        card_num = 'not num'
    
    if type(card_num) == int and len(message.text) == 16:
        addWallet_db(message, 'G')
        await dp.bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id-1)
        await message.answer(f"{message.text} kartangiz yaroqlik muddatini kiriting\n\nFormat: 01/23 yoki 0123")    
        await EditWallet.EditUzcardDate.set()
    
    elif card_num == 'not num' or len(message.text) != 16:
        await message.answer("UZCARD kartangiz ustidagi 16 talik raqamni kiriting!")
            
    
@dp.message_handler(state = EditWallet.EditUzcardDate)
async def change(message: types.Message, state:FSMContext):
    if len(message.text) == 5:
        await message.answer("Karta muvaffaqqiyatli qo'shildi", reply_markup = addWallet)
        addWallet_db(message, 'H')
        await Map.hamyonlar.set()
    
    elif len(message.text) == 4:
        uzcard_date = message.text[:2] + '/' + message.text[2:]
        addWallet_db(message, 'H')
        await message.answer("Karta muvaffaqqiyatli qo'shildi", reply_markup=addWallet)
        await Map.hamyonlar.set()
    
    else:
        await message.answer("Noto'gri format kiritdingiz!\n\nFormat: 01/23 yoki 0123 kabi kiriting")
        

### Add HUMO
@dp.message_handler(state = EditWallet.EditHumo)
async def change(message: types.Message, state:FSMContext):
    card_num = message.text

    try:
        card_num = int(card_num)   
    except:
        card_num = 'not num'
    
    if type(card_num) == int and len(message.text) == 16:
        addWallet_db(message, 'I')
        await dp.bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id-1)
        await message.answer(f"{message.text} kartangiz yaroqlik muddatini kiriting\n\nFormat: 01/23 yoki 0123")    
        await EditWallet.EditHumoDate.set()
    
    elif card_num == 'not num' or len(message.text) != 16:
        await message.answer("HUMO kartangiz ustidagi 16 talik raqamni kiriting!")
        
    
@dp.message_handler(state = EditWallet.EditHumoDate)
async def change(message: types.Message, state:FSMContext):    
    if len(message.text) == 5:
        addWallet_db(message, 'J')
        await dp.bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id-1)
        await message.answer("Karta muvaffaqqiyatli qo'shildi✅", reply_markup = addWallet)
        await Map.hamyonlar.set()
    
    elif len(message.text) == 4:
        uzcard_date = message.text[:2] + '/' + message.text[2:]
        addWallet_db(message, 'J')
        await message.answer("Karta muvaffaqqiyatli qo'shildi✅", reply_markup=addWallet)
        await Map.hamyonlar.set()
    
    else:
        await message.answer("Noto'gri format kiritdingiz!\n\nFormat: 01/23 yoki 0123 kabi kiriting")
        
### Add QIWI
@dp.message_handler(state = EditWallet.EditQiwi)
async def change(message: types.Message, state:FSMContext):
    qiwi_num = message.text[1:]

    try:
        if message.text[0] == '+':
            qiwi_num = int(qiwi_num)     
    except:
        qiwi_num = 'not num'
    
    if type(qiwi_num) == int and len(message.text) >= 10:
        addWallet_db(message, 'K')
        await message.answer("Qiwi hisob muvaffaqqiyatli qo'shildi✅", reply_markup=addWallet)        
        await Map.hamyonlar.set()
    
    elif qiwi_num == 'not num' or len(message.text) != 13:
        await message.answer('QIWI hamyoningiz raqamini kiriting.\n\nFormat: +998901234567')


### Add WMZ        
@dp.message_handler(state = EditWallet.EditWMZ)
async def change(message: types.Message, state:FSMContext):
    wmz_num = message.text[1:]

    if message.text[0] == 'Z' or message.text[0] == 'z':
        try:
            wmz_num = int(wmz_num)
        except:
            pass
    else:
        wmz_num = 'not num'
    
    if type(wmz_num) == int and len(message.text) > 10:
        await message.answer("WMZ hisob muvaffaqqiyatli qo'shildi✅", reply_markup=addWallet)
        addWallet_db(message, 'L')
        await Map.hamyonlar.set()
    
    elif wmz_num == 'not num' or len(message.text) <= 10:
        await message.answer('WMZ hamyoningiz raqamini kiriting.\n\nFormat: Z123456789012')

### Add WMR
@dp.message_handler(state = EditWallet.EditWMR)
async def change(message: types.Message, state:FSMContext):
    wmr_num = message.text[1:]
    
    if message.text[0] == 'R' or message.text[0] == 'r':
        try:
            wmr_num = int(wmr_num)
        except:
            pass
    else:
        wmr_num = 'not num'
    
    if type(wmr_num) == int and len(message.text) > 10:
        addWallet_db(message, 'M')
        await message.answer("WMR hisob muvaffaqqiyatli qo'shildi✅", reply_markup=addWallet)
        await Map.hamyonlar.set()
    
    elif wmr_num == 'not num' or len(message.text) <= 10:
        await message.answer('WMR hamyoningiz raqamini kiriting.\n\nFormat: R123456789012')


### Add Payeer
@dp.message_handler(state = EditWallet.EditPayeer)
async def change(message: types.Message, state:FSMContext):
    payeer_num = message.text[1:]
    
    if message.text[0] == 'P' or message.text[0] == 'p':
        try:
            payeer_num = int(payeer_num)
        except:
            pass
    else:
        payeer_num = 'not num'
    
    if type(payeer_num) == int and len(message.text) > 6:
        await message.answer("Payeer hisob muvaffaqqiyatli qo'shildi✅", reply_markup=addWallet)
        addWallet_db(message, 'N')
        await Map.hamyonlar.set()
    
    elif payeer_num == 'not num' or len(message.text) <= 6:
        addWallet_db(message, 'N')
        await message.answer('PAYEER hamyoningiz raqamini kiriting.\n\nFormat: P1234567890')


#Add Yandex
@dp.message_handler(state = EditWallet.EditYandex)
async def change(message: types.Message, state:FSMContext):
    yandex_num = message.text
    if len(yandex_num) > 10:
        try:
            yandex_num = int(yandex_num)
        except:
            pass
    else:
        yandex_num = 'not num'
    
    if type(yandex_num) == int and len(message.text) > 10:
        addWallet_db(message, 'O')
        await message.answer("Yandex hisob muvaffaqqiyatli qo'shildi✅", reply_markup=addWallet)
        await Map.hamyonlar.set()
    
    elif yandex_num == 'not num' or len(message.text) <= 10:
        await message.answer('YANDEX hamyoningiz raqamini kiriting.\n\nFormat: 12345678901234')


#Add Sberbank
@dp.message_handler(state = EditWallet.EditSberbank)
async def change(message: types.Message, state:FSMContext):
    sberbank_num = message.text
    if len(sberbank_num) > 10:
        try:
            sberbank_num = int(sberbank_num)
        except:
            pass
    else:
        sberbank_num = 'not num'
    
    if type(sberbank_num) == int and len(message.text) > 14:
        await message.answer("Сбербанк hisob muvaffaqqiyatli qo'shildi✅", reply_markup=addWallet)
        addWallet_db(message, 'P')
        await Map.hamyonlar.set()

    elif sberbank_num == 'not num' or len(message.text) <= 14:
        await message.answer('Сбербанк hamyoningiz raqamini kiriting.\n\nFormat: 1234567890123456')
        

#Add Tinkoff
@dp.message_handler(state = EditWallet.EditTinkoff)
async def change(message: types.Message, state:FSMContext):
    tinkoff_num = message.text
    if len(tinkoff_num) > 15:
        try:
            tinkoff_num = int(tinkoff_num)
        except:
            pass
    else:
        tinkoff_num = 'not num'
    
    if type(tinkoff_num) == int and len(message.text) > 14:
        addWallet_db(message, 'Q')
        await message.answer("Тинкофф hisob muvaffaqqiyatli qo'shildi✅", reply_markup=addWallet)
        await Map.hamyonlar.set()
    
    elif tinkoff_num == 'not num' or len(message.text) <= 15:
        await message.answer('Тинкофф hamyoningiz raqamini kiriting.\n\nFormat: 1234567890123456')
        

@dp.callback_query_handler(state = Map.hamyonlar, text = 'clear_wallets')
async def walletClear(call:types.CallbackQuery):
    clearWallets(call)
    await call.message.edit_text("Malumotlar o'chirildi✅")