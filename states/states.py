from aiogram.dispatcher.filters.state import State, StatesGroup


class MainState(StatesGroup):
    type = State()
    number_def = State()
    number_cop = State()
    number_dip = State()
    number_voe = State()