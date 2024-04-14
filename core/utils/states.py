from aiogram.fsm.state import State, StatesGroup
class Send(StatesGroup):
    page = State()
    sub = State()
    name = State()
    photo = State()