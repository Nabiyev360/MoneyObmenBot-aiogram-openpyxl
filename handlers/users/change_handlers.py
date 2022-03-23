from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery

from loader import dp
from keyboards.inline.choosevaluta import *
from keyboards.inline.chooseGiveTake import givOrTake
from utils.db_api.dbxl import getWalletData, getTransferId


### Kerakli funksiyalar
async def from_updater(id, state, FROM):
    """Berishni saqlovchi funksiya"""
    berish = f"ber_{id}"
    await state.update_data(
        {berish:FROM} 
        )

markupDict = {"uzcard":chooseUzcard, "humo":chooseHumo, "qiwi":chooseQiwi, "wmz":chooseWmz, "wmr":chooseWmr, "yandex":chooseYandexRub, "payeer_rub":choosePayeerRub, "payeer_usd":choosePayeerUsd, "tinkoff":chooseTinkoffRub, "sberbank":chooseSberbankRub}

valutas = {"uzcard":"UZCARD", "humo":"HUMO", "qiwi":"QIWI RUB", "wmz":"WMZ", "wmr":"WMR", "yandex":"YANDEX RUB", "payeer_rub":"PAYEER RUB", "payeer_usd":"PAYEER USD", "tinkoff":"Тинкофф RUB", "sberbank":"Сбербанк RUB"}


### Berish strok
@dp.callback_query_handler(text_contains = 'from_')
async def choose1(call: CallbackQuery, state = FSMContext):
    await from_updater(call.from_user.id, state, call.data[5:])
    await call.message.edit_reply_markup(reply_markup = markupDict[call.data[5:]])

### Olish strok
@dp.callback_query_handler(text_contains = 'to_')
async def choose2(call: CallbackQuery, state = FSMContext):
    olish = call.data[3:]
    await state.update_data(
        {f"ol_{call.from_user.id}":olish}       #giv_take_handlersda ishlatish uchun qo'shilyapti
        )    
        
    # Ma'lumotlarni qayta o'qiymiz va userga ko'rsatamiz
    datas = await state.get_data()
    berish = datas.get(f"ber_{call.from_user.id}")

    if getWalletData(call.from_user.id, olish) != None and getWalletData(call.from_user.id, berish) != None:
        if olish == 'qiwi':
            text = (f"Identifikatsiya bo'lanmagan hamyonlarga almashuv ochish mumkin emas! Ochilsa -50% bilan almashuv miqdoringiz qaytariladi. Iltimos shuni inobatga oling.\n",
                "<b>Almashuv:</b>",
                f"ID: <code>{getTransferId()}</code>",
                f"Berish: * {valutas[berish]}",
                f"Olish: * {valutas[olish]}",
                f"<b>{valutas[berish]}: {getWalletData(call.from_user.id, berish)}</b>",
                f"<b>{valutas[olish]}: {getWalletData(call.from_user.id, olish)}</b>")
        else:
            text = (f"<b>Almashuv:</b>",
                f"ID: <code>{getTransferId()}</code>",
                f"Berish: * {valutas[berish]}",
                f"Olish: * {valutas[olish]}",
                f"<b>{valutas[berish]}: {getWalletData(call.from_user.id, berish)}</b>",
                f"<b>{valutas[olish]}: {getWalletData(call.from_user.id, olish)}</b>")
        await call.message.answer("\n".join(text), reply_markup = givOrTake(valutas[berish], valutas[olish]))

    else:
        await call.answer("Siz tanlagan yo'nalishda almashuvni amalga oshirish uchun oldin o'z hamyonlaringizni 🗂Hamyonlar bo'limiga kiriting", show_alert=True)
    await call.message.delete() 