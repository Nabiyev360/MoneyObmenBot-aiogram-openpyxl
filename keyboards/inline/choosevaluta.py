from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class ChooseValuta:
    def __init__(self, l_valuta1 = "🔼UZCARD", l_valuta2 = "🔼HUMO", l_valuta3 = "🔼QIWI RUB", 
    l_valuta4 = "🔼WMZ", l_valuta5 = "🔼WMR", l_valuta6 = "🔼YANDEX RUB", l_valuta7 = "🔼PAYEER RUB", 
    l_valuta8 = "🔼PAYEER USD", l_valuta9 = "🔼Тинкофф RUB", l_valuta10 = "🔼Сбербанк RUB", 
    r_valuta1 = "▫️", r_valuta2 = "▫️", r_valuta3 = "▫️", r_valuta4 = "▫️", 
    r_valuta5 = "▫️", r_valuta6 = "▫️", r_valuta7 = "▫️", r_valuta8 = "▫️", 
    r_valuta9 = "▫️", r_valuta10 = "▫️",  callback1 = "none", callback2 = "none", callback3 = "none", callback4 = "none", callback5 = "none", callback6 = "none", 
    callback7 = "none", callback8 = "none", callback9 = "none", callback10 = "none"):
        self.l_valuta1 = l_valuta1
        self.l_valuta2 = l_valuta2
        self.l_valuta3 = l_valuta3
        self.l_valuta4 = l_valuta4
        self.l_valuta5 = l_valuta5
        self.l_valuta6 = l_valuta6
        self.l_valuta7 = l_valuta7
        self.l_valuta8 = l_valuta8
        self.l_valuta9 = l_valuta9
        self.l_valuta10 = l_valuta10
        
        self.r_valuta1 = r_valuta1
        self.r_valuta2 = r_valuta2
        self.r_valuta3 = r_valuta3
        self.r_valuta4 = r_valuta4
        self.r_valuta5 = r_valuta5
        self.r_valuta6 = r_valuta6
        self.r_valuta7 = r_valuta7
        self.r_valuta8 = r_valuta8
        self.r_valuta9 = r_valuta9
        self.r_valuta10 = r_valuta10
        
        self.callback1 = callback1
        self.callback2 = callback2
        self.callback3 = callback3
        self.callback4 = callback4
        self.callback5 = callback5
        self.callback6 = callback6
        self.callback7 = callback7
        self.callback8 = callback8
        self.callback9 = callback9
        self.callback10 = callback10
        

        
    def makeValuta(self):
        chooseValuta = InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(text = self.l_valuta1, callback_data = 'from_uzcard'),
                InlineKeyboardButton(text = self.r_valuta1, callback_data = self.callback1)
            ],
            [
                InlineKeyboardButton(text = self.l_valuta2, callback_data = 'from_humo'),
                InlineKeyboardButton(text = self.r_valuta2, callback_data = self.callback2)
            ],
            [  
                InlineKeyboardButton(text = self.l_valuta3, callback_data = 'from_qiwi'),
                InlineKeyboardButton(text = self.r_valuta3, callback_data = self.callback3)
            ],
            [
                InlineKeyboardButton(text = self.l_valuta4, callback_data = 'from_wmz'),
                InlineKeyboardButton(text = self.r_valuta4, callback_data = self.callback4)
            ],
            [    
                InlineKeyboardButton(text = self.l_valuta5, callback_data = 'from_wmr'),
                InlineKeyboardButton(text = self.r_valuta5, callback_data = self.callback5)
            ],
            [    
                InlineKeyboardButton(text = self.l_valuta6, callback_data = 'from_yandex'),
                InlineKeyboardButton(text = self.r_valuta6, callback_data = self.callback6)
            ],
            [    
                InlineKeyboardButton(text = self.l_valuta7, callback_data = 'from_payeer_rub'),
                InlineKeyboardButton(text = self.r_valuta7, callback_data = self.callback7)
            ],
            [    
                InlineKeyboardButton(text = self.l_valuta8, callback_data = 'from_payeer_usd'),
                InlineKeyboardButton(text = self.r_valuta8, callback_data = self.callback8)
            ],
            [   
                InlineKeyboardButton(text = self.l_valuta9, callback_data = 'from_tinkoff'),
                InlineKeyboardButton(text = self.r_valuta9, callback_data = self.callback9)
            ],
            [    
                InlineKeyboardButton(text = self.l_valuta10, callback_data = 'from_sberbank'),
                InlineKeyboardButton(text = self.r_valuta10, callback_data = self.callback10)
            ]        
    ])
    
        return chooseValuta


        

choose_menu = ChooseValuta()
chooseValuta = choose_menu.makeValuta()

choose_uzcard = ChooseValuta(l_valuta1='✅UZCARD', r_valuta1='🔽WMR', r_valuta2="🔽WMZ", 
r_valuta3="🔽YANDEX RUB", r_valuta4="🔽QIWI RUB", r_valuta5="🔽PAYEER RUB", 
r_valuta6="🔽PAYEER USD", r_valuta7="🔽Тинкофф RUB", r_valuta8="🔽Сбербанк RUB", 
callback1="to_wmr", callback2="to_wmz", callback3='to_yandex', callback4='to_qiwi', callback5='to_payeer_rub', callback6="to_payeer_usd", callback7="to_tinkoff", callback8='to_sberbank')

chooseUzcard = choose_uzcard.makeValuta()

choose_humo = ChooseValuta(l_valuta2='✅HUMO', r_valuta1='🔽WMR', r_valuta2="🔽WMZ", 
r_valuta3="🔽YANDEX RUB", r_valuta4="🔽QIWI RUB", r_valuta5="🔽PAYEER RUB", r_valuta6="🔽PAYEER USD", r_valuta7="🔽Тинкофф RUB", r_valuta8="🔽Сбербанк RUB", 
callback1="to_wmr", callback2="to_wmz", callback3='to_yandex', callback4='to_qiwi', callback5='to_payeer_rub', callback6="to_payeer_usd", callback7="to_tinkoff", callback8='to_sberbank'
    )
chooseHumo = choose_humo.makeValuta()

choose_qiwi = ChooseValuta(
    l_valuta3='✅QIWI RUB', r_valuta1='🔽UZCARD', r_valuta2="🔽HUMO", 
    r_valuta3="🔽WMR", r_valuta4="🔽YANDEX RUB", r_valuta5="🔽PAYEER RUB", r_valuta6="🔽Тинкофф RUB", r_valuta7="🔽Сбербанк RUB", 
    callback1="to_uzcard", callback2="to_humo", callback3='to_wmr', callback4='to_yandex', callback5='to_payeer_rub', callback6="to_tinkoff", callback7="to_sberbank"
    )
chooseQiwi = choose_qiwi.makeValuta()

choose_wmz = ChooseValuta(
    l_valuta4='✅WMZ', r_valuta1='🔽UZCARD', r_valuta2="🔽HUMO", r_valuta3="🔽PAYEER USD",
    callback1="to_uzcard", callback2="to_humo", callback3='to_payeer_usd'
    )
chooseWmz = choose_wmz.makeValuta()

choose_wmr = ChooseValuta(
    l_valuta5='✅WMR', r_valuta1='🔽UZCARD', r_valuta2="🔽HUMO",
    r_valuta3="🔽QIWI RUB", r_valuta4="🔽YANDEX RUB", r_valuta5="🔽PAYEER RUB", r_valuta6="🔽Тинкофф RUB", r_valuta7="🔽Сбербанк RUB",
    callback1="to_uzcard", callback2="to_humo", callback3='to_qiwi', callback4='to_yandex', callback5='to_payeer_rub', callback6="to_tinkoff", callback7="to_sberbank"    
)
chooseWmr = choose_wmr.makeValuta()

choose_yandex_rub = ChooseValuta(
    l_valuta6='✅YANDEX RUB', r_valuta1='🔽UZCARD', r_valuta2="🔽HUMO",
    r_valuta3="🔽WMR", r_valuta4="🔽QIWI RUB", r_valuta5="🔽PAYEER RUB", r_valuta6="🔽Тинкофф RUB", r_valuta7="🔽Сбербанк RUB",
    callback1="to_uzcard", callback2="to_humo", callback3='to_wmr', callback4='to_qiwi', callback5='to_payeer_rub', callback6="to_tinkoff", callback7="to_sberbank"    
)
chooseYandexRub = choose_yandex_rub.makeValuta()

choose_payeer_rub = ChooseValuta(
    l_valuta7='✅PAYEER RUB', r_valuta1='🔽UZCARD', r_valuta2="🔽HUMO",
    r_valuta3="🔽WMR", r_valuta4="🔽QIWI RUB", r_valuta5="🔽YANDEX RUB", r_valuta6="🔽Тинкофф RUB", r_valuta7="🔽Сбербанк RUB",
    callback1="to_uzcard", callback2="to_humo", callback3='to_wmr', callback4='to_qiwi', callback5='to_payeer_rub', callback6="to_tinkoff", callback7="to_sberbank" 
)
choosePayeerRub = choose_payeer_rub.makeValuta()

choose_payeer_usd = ChooseValuta(
    l_valuta8='✅PAYEER USD', r_valuta1='🔽UZCARD', r_valuta2="🔽HUMO",
    r_valuta3="🔽WMZ",
    callback1="to_uzcard", callback2="to_humo", callback3='to_wmz'
)
choosePayeerUsd = choose_payeer_usd.makeValuta()

choose_tinkoff_rub = ChooseValuta(
    l_valuta9='✅Тинкофф RUB', r_valuta1='🔽UZCARD', r_valuta2="🔽HUMO",
    r_valuta3="🔽WMR", r_valuta4="🔽QIWI RUB", r_valuta5="🔽YANDEX RUB", r_valuta6="🔽PAYEER RUB" , r_valuta7="🔽Сбербанк RUB",
    callback1="to_uzcard", callback2="to_humo", callback3='to_wmr', callback4='to_qiwi', callback5='to_yandex', callback6="to_payeer_rub", callback7="to_sberbank" 
)
chooseTinkoffRub = choose_tinkoff_rub.makeValuta()

choose_sberbank_rub = ChooseValuta(
    l_valuta10='✅Сбербанк RUB', r_valuta1='🔽UZCARD', r_valuta2="🔽HUMO",
    r_valuta3="🔽WMR", r_valuta4="🔽QIWI RUB", r_valuta5="🔽YANDEX RUB", r_valuta6="🔽PAYEER RUB" , r_valuta7="🔽Тинкофф RUB",
    callback1="to_uzcard", callback2="to_humo", callback3='to_wmr', callback4='to_qiwi', callback5='to_yandex', callback6="to_payeer_rub", callback7="to_tinkoff"
)
chooseSberbankRub = choose_sberbank_rub.makeValuta()