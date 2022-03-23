from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from loader import dp
from data.config import ADMINS
from states.berishOlishSum import BerSum, OlSum
from handlers.users.change_handlers import valutas
from keyboards.default.main_menu import mainMenu
from keyboards.inline.pay import payOrCancel, payedOrCancel
from keyboards.inline.cancel import Cancel
from keyboards.inline.adminResult import success_or_fail
from utils.db_api.dbxl import getWalletData, get_data, getTransferId, addOperation

pul_birligi = {"uzcard":"SO'M", "humo":"SO'M", "qiwi":"RUB", "wmz":"USD", "wmr":"RUB", "yandex":"RUB", "payeer_rub":"RUB", "payeer_usd":"USD", "tinkoff":"RUB", "sberbank":"RUB"}

kassaWallet = {"uzcard":"8600312984121521", "humo":"9860350102090288", "qiwi":"+998930097749", "wmz":"Z547121102276", "wmr":"R624293230623", "yandex":"4100116158678160", "payeer_rub":"P1035817455", "payeer_usd":"P1035817455", "tinkoff":"1111222233334444", "sberbank":"5555666677778888"}

def llimiter(type, givtake='choose_berish'):   # Olishni kiritishga alohida limit sharti yozish kerak
    if givtake == 'choosen_berish':
        if pul_birligi[type] == "SO'M":
            min_sum = get_data('X2')
            max_sum = get_data('Y2')
        elif pul_birligi[type] == "RUB":
            min_sum = get_data('X3')
            max_sum = get_data('Y3')
        elif pul_birligi[type] == "USD":
            min_sum = get_data('X4')
            max_sum = get_data('Y4')
        text = (f"Berish miqdorini {pul_birligi[type]} birligida kiriting:", 
        f"Minimal: <code>{min_sum}</code>",
        f"Maksimal: <code>{max_sum}</code>")  
    
    elif givtake == 'choosen_olish':
        if pul_birligi[type] == "SO'M":
            min_sum = get_data('X2')
            max_sum = get_data('Y2')
        elif pul_birligi[type] == "RUB":
            min_sum = get_data('X3')
            max_sum = get_data('Y3')
        elif pul_birligi[type] == "USD":
            min_sum = get_data('X4')
            max_sum = get_data('Y4')
        text = (f"Berish miqdorini {pul_birligi[type]} birligida kiriting:", 
        f"Minimal: <code>{min_sum}</code>",
        f"Maksimal: <code>{max_sum}</code>")
    
    return text, min_sum, max_sum
    

@dp.callback_query_handler(text = 'choosen_berish')
async def berKirit(call: CallbackQuery, state:FSMContext):
    datas = await state.get_data()      # Vaqtinchalik ma'lumotlarni qayta o'qiymiz
    berish = datas.get(f"ber_{call.from_user.id}")
    text = llimiter(berish, 'choosen_berish')[0]
    await call.message.answer("\n".join(text), reply_markup = Cancel)
    await call.message.delete()
    await BerSum.berish_sum.set()


@dp.callback_query_handler(text = 'choosen_olish')
async def olKirit(call: CallbackQuery, state:FSMContext):  
    datas = await state.get_data()           # Vaqtinchalik ma'lumotlarni qayta o'qiymiz
    olish = datas.get(f"ol_{call.from_user.id}")
    text = llimiter(olish, 'choosen_olish')[0]    
    await call.message.answer("\n".join(text), reply_markup = Cancel)
    await call.message.delete()
    await OlSum.olish_sum.set()
    


@dp.message_handler(state = BerSum)
async def viewSumma(message: Message, state: FSMContext):
   
    datas = await state.get_data()      # Vaqtinchalik ma'lumotlarni qayta o'qiymiz
    berish = datas.get(f"ber_{message.from_user.id}")
    olish = datas.get(f"ol_{message.from_user.id}")
    
    text = llimiter(berish, 'choosen_berish')[0]
    limit_min = llimiter(berish, 'choosen_berish')[1]
    limit_max = llimiter(berish, 'choosen_berish')[2]

    try:
        if int(message.text) >= limit_min and int(message.text) <= limit_max:

            if pul_birligi[berish] == "SO'M" and pul_birligi[olish] == "RUB":
                kurs = get_data('T4')
                olish_sum = round(int(message.text) / kurs, 2)
            
            elif pul_birligi[berish] == "SO'M" and pul_birligi[olish] == "USD":
                kurs = get_data('T5')
                olish_sum = round(int(message.text) / kurs, 2)
                
            elif pul_birligi[berish] == 'RUB'and pul_birligi[olish] == "SO'M":
                kurs = get_data('U4')
                olish_sum = round(int(message.text) * kurs, 2)
            
            elif pul_birligi[berish] == 'USD'and pul_birligi[olish] == "SO'M":
                kurs = get_data('U5')
                olish_sum = round(int(message.text) * kurs, 2)
            
            elif pul_birligi[berish] == "RUB" and pul_birligi[olish] == "RUB":
                kurs = get_data('T11')
                olish_sum = round(int(message.text) * kurs, 2)
            
            elif pul_birligi[berish] == 'USD'and pul_birligi[olish] == "USD":
                kurs = get_data('T12')
                olish_sum = round(int(message.text) * kurs, 2)
            
            # elif olish=='wmz' or olish=='payeer_usd':
            #     kurs = get_data('U5')
            #     olish_sum = round(int(message.text) / kurs, 2)


            await state.update_data(
                {'userdan_sum': f"{message.text} {pul_birligi[berish]}",
                 'userga_sum': f"{olish_sum} {pul_birligi[olish]}"}
            )
            
            text = ("<b>Almashuv</b>", 
                f"ID: <code>{getTransferId()}</code>", 
                f"Berish: {message.text} {pul_birligi[berish]}", 
                f"Olish: {olish_sum} {pul_birligi[olish]}", 
                f"<b>{valutas[berish]}: {getWalletData(message.from_user.id, berish)}</b>", 
                f"<b>{valutas[olish]}: {getWalletData(message.from_user.id, olish)}</b>")
            await message.answer("\n".join(text), reply_markup = payOrCancel)
           
            await dp.bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id-1)
        else:
            i = 0/0     # Xatolik keltirib chiqarish uchun
            
    except:
        await message.answer("\n".join(text), reply_markup = Cancel)
    

    
@dp.message_handler(state = OlSum)
async def viewSumma(message: Message, state: FSMContext):
    datas = await state.get_data()      # Vaqtinchalik ma'lumotlarni qayta o'qiymiz
    berish = datas.get(f"ber_{message.from_user.id}")
    olish = datas.get(f"ol_{message.from_user.id}")
    
    text = llimiter(olish, 'choosen_olish')[0]
    limit_min = llimiter(olish, 'choosen_olish')[1]
    limit_max = llimiter(olish, 'choosen_olish')[2]

    try:
        if int(message.text) >= limit_min and int(message.text) <= limit_max:
            
            if pul_birligi[berish] == "SO'M" and pul_birligi[olish] == "RUB":
                kurs = get_data('T4')
                berish_sum = round(int(message.text) * kurs, 2)
            
            elif pul_birligi[berish] == "SO'M" and pul_birligi[olish] == "USD":
                kurs = get_data('T5')
                berish_sum = round(int(message.text) * kurs, 2)
                
            elif pul_birligi[berish] == 'RUB'and pul_birligi[olish] == "SO'M":
                kurs = get_data('U4')
                berish_sum = round(int(message.text) / kurs, 2)
            
            elif pul_birligi[berish] == 'USD'and pul_birligi[olish] == "SO'M":
                kurs = get_data('U5')
                berish_sum = round(int(message.text) / kurs, 2)
            
            elif pul_birligi[berish] == "RUB" and pul_birligi[olish] == "RUB":
                kurs = get_data('T11')
                berish_sum = round(int(message.text) / kurs, 2)
            
            elif pul_birligi[berish] == 'USD'and pul_birligi[olish] == "USD":
                kurs = get_data('T12')
                berish_sum = round(int(message.text) / kurs, 2)
            
            # elif olish=='wmz' or olish=='payeer_usd':
            #     kurs = get_data('U5')
            #     olish_sum = round(int(message.text) / kurs, 2)


            await state.update_data(
                {'userdan_sum': f"{berish_sum} {pul_birligi[berish]}",
                 'userga_sum':f"{message.text} {pul_birligi[olish]}"}
            )
            
            
            text = ("<b>Almashuv</b>", 
            f"ID: <code>{getTransferId()}</code>", 
            f"Berish: {berish_sum} {pul_birligi[berish]}", 
            f"Olish: {message.text} {pul_birligi[olish]}", 
            f"<b>{valutas[berish]}: {getWalletData(message.from_user.id, berish)}</b>", 
            f"<b>{valutas[olish]}: {getWalletData(message.from_user.id, olish)}</b>")
            await message.answer("\n".join(text), reply_markup = payOrCancel)
           
            await dp.bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id-1)
        else:
            i = 0/0     # Xatolik keltirib chiqarish uchun
            
    except:
        await message.answer("\n".join(text), reply_markup = Cancel)



@dp.callback_query_handler(text = 'pay', state = [BerSum, OlSum])
async def pay(call: CallbackQuery, state:FSMContext):
    datas = await state.get_data()             # Vaqtinchalik ma'lumotlarni qayta o'qiymiz
    berish = datas.get(f"ber_{call.from_user.id}")
    userdan_sum = datas.get(f"userdan_sum")
    
    await call.message.answer(kassaWallet[berish])
    await call.message.answer(f"👆Ko'chirib olish uchun \n\nAlmashuvingiz muvaffaqiyatli bajarilishi uchun quyidagi harakatlarni amalga oshiring:\n\n1) Pastda ko'rsatilgan to'lov miqdorni  -  {kassaWallet[berish]}  raqamiga o'tkazing;\n\n2) «To'lov qildim ✅» tugmasini bosing; \n3) Operator tomonidan almashuv tasdiqlanishini kuting.\n\n\n <b>To'lov miqdori: {userdan_sum}</b> \n\nUshbu almashuv operator tomonidan navbati bilan amalga oshiriladi va 2 daqiqadan 30 daqiqagacha davom etadi.", reply_markup = payedOrCancel)
    await call.message.delete()
    


@dp.callback_query_handler(text = 'payed', state = [BerSum, OlSum])
async def pay(call: CallbackQuery, state:FSMContext):
    await call.message.delete()
    await dp.bot.delete_message(chat_id = call.from_user.id, message_id=call.message.message_id-1)  #delete WalletNumni o'chiradi
    
    datas = await state.get_data()             # Vaqtinchalik ma'lumotlarni qayta o'qiymiz
    berish = datas.get(f"ber_{call.from_user.id}")
    olish = datas.get(f"ol_{call.from_user.id}")
    userdan_sum = datas.get(f"userdan_sum")
    userga_sum = datas.get(f"userga_sum")
    
    await state.finish()            # Userni state'dan chiqaramiz
    
    await call.message.answer(
        text = f"<b>Almashuv ID: {getTransferId()} </b>\nBuyurtmangiz operatorga yuborildi, iltimos tasdiqlanishini kuting!", reply_markup=mainMenu)

    text = ("<b>Almashuv</b>", 
        f"<b>ID</b>: {getTransferId()}", 
        f"{valutas[berish]} --> {valutas[olish]}",
        f"User {valutas[berish]} Num: {getWalletData(call.from_user.id, berish)}",
        f"User {valutas[olish]} Num: {getWalletData(call.from_user.id, olish)}",
        f"Userdan summa: {userdan_sum}",
        f"Userga summa: {userga_sum}"
        )
    
    await dp.bot.send_message(ADMINS[0], "\n".join(text), reply_markup=success_or_fail)
    
    # Bazaga qo'shish
    addOperation(valutas[berish],
        valutas[olish],
        getWalletData(call.from_user.id, berish),
        getWalletData(call.from_user.id, olish),
        f"{userdan_sum}",
        f"{userga_sum}",
        call.from_user.full_name,
        call.from_user.username,
        call.from_user.id
        )
