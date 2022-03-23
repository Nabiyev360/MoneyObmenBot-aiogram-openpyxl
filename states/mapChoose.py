from aiogram.dispatcher.filters.state import StatesGroup, State

class ChooseWallets(StatesGroup):
    Berish = State()
    Olish = State()
    
    
    EditUzcard = State()
    EditHumo = State()
    EditQiwi = State()
    EditPayeer = State()
    EditWMZ = State()
    EditWMR = State()
    EditYandex = State()
    EditTinkoff = State()
    EditSeberbank = State()