from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.mapMenu import Map
from utils.db_api.dbxl import getWalletData
from keyboards.inline.choosevaluta import chooseValuta
from keyboards.default.wallet_keyboard import addWallet
from keyboards.inline.wallet_inline import clearWallets
from keyboards.inline.supportLink import go_support

@dp.message_handler(text = ['♻️ Valyuta ayirboshlash', '🗂Hamyonlar', '📈Kurs | Zahira', '🔁Almashinuvlar', 'ℹ️Ma\'lumotlar', '🍋QIWI identifikatsiya', '👥Referallar', '👨🏻‍💻Aloqa'], state="*")
async def change(message: types.Message, state:FSMContext):
    await state.finish()
    
    if message.text == '♻️ Valyuta ayirboshlash':
        await message.answer('⬆️Berish va ⬇️Olish valyutalarini tanlang', reply_markup = chooseValuta)
        
    elif message.text == '🗂Hamyonlar':
        await message.answer('🗂Hisoblar:', reply_markup=addWallet)
        
        uzcardNum = getWalletData(message.chat.id, 'uzcard')
        humoNum = getWalletData(message.chat.id, 'humo')
        qiwiNum = getWalletData(message.chat.id, 'qiwi')
        wmzNum = getWalletData(message.chat.id, 'wmz')
        wmrNum = getWalletData(message.chat.id, 'wmr')
        payeerNum = getWalletData(message.chat.id, 'payeer')
        yandexNum = getWalletData(message.chat.id, 'yandex')
        sberbankNum = getWalletData(message.chat.id, 'sberbank')
        tinkoffNum = getWalletData(message.chat.id, 'tinkoff')
        
        wallets = f"<b>📌UZCARD</b>:\n{uzcardNum}\n<b>📌HUMO:</b>\n{humoNum}\n<b>📌QIWI:</b>\n{qiwiNum}\n<b>📌WMZ</b>:\n{wmzNum}\n<b>📌WMR:</b>\n{wmrNum}\n<b>📌PAYEER:</b>\n{payeerNum}\n<b>📌YANDEX:</b>\n{yandexNum}\n<b>📌Сбербанк:</b>\n{sberbankNum}\n<b>📌Тинкофф:</b>\n{tinkoffNum}"
        await message.answer(wallets, reply_markup = clearWallets)
        await Map.hamyonlar.set()
            
    elif message.text == '📈Kurs | Zahira':
        await message.answer("📉Sotish kursi \n1 QIWI RUB = 152 UZS \n1 PAYEER RUB = 152 UZS \n1 PAYEER USD = 11000 UZS \n1 Yandex RUB = 148 UZS \n1 WMZ = 11200 UZS \n1 WMR = 148 UZS \n\n📉Olish kursi \n1 QIWI RUB = 130 UZS \n1 PAYEER RUB = 132 UZS \n1 PAYEER USD = 9500 UZS \n1 Yandex RUB = 110 UZS \n1 WMZ = 9800 UZS \n1 WMR = 128 UZS")
        
    elif message.text == '🔁Almashinuvlar':
            await message.answer("Almashinuvlar tarixi bo'sh!")

    elif message.text == 'ℹ️Ma\'lumotlar':
        await message.answer('▪️ MoneyObmen - bu ishonchli UZCARD va elektron hamyonlar almashuv xizmati.\n\nDasturchi: @NabiyevDev')
        
    elif message.text == '🍋QIWI identifikatsiya':
        text = "🔖 QIWI hamyon Identifikatsiyasi.\n\nBizning servis mijozlarga QIWI  hamyon statusini Identifikatsiya qilish xizmatini taqdim qiladi.\n\nOsnovnoy Status\nXizmat narxi: 150 RUB\n\nProfessionalny Status:\nXizmat narxi: 1100 RUB\nKerakli hujjatlar:\n- Pasport asosiy beti rasmi.\n- Pasport propiska beti rasmi.\n- QIWI hamyon raqami.\n\nIdentifikatsiyadan o'tish uchun qo'llab quvvatlash markaziga murojat qiling.️️"
        await message.answer(text, reply_markup=go_support)
        
    
    elif message.text == '👥Referallar':
        await message.answer(f"💵Sizning hisobingiz: 0 UZS \nDo'stlarni taklif qiling va sizning tavsiyangiz bo'yicha o'tkaziladigan har bir almashuv daromadidan 10% olasiz \n\nSizning link: t.me/MoneyObmenbot?start={message.from_user.id}")


    elif message.text == '👨🏻‍💻Aloqa':
        await message.answer("Xizmatimizga tegishli savollar/takliflaringiz bo'lsa bilan bog'laning. Biz bilan aloqa: Qo'llab-quvvatlash xizmati: @NabiyevDev")