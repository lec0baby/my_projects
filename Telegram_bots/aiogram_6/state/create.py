from aiogram.fsm.state import StatesGroup, State


class CreateState(StatesGroup):
    place = State()
    data = State()
    time = State()
    minplayer = State()
    maxplayer = State()
    price = State()