from aiogram.fsm.state import State, StatesGroup

class Bid(StatesGroup):
    service = State()
    name = State()
    phone_number = State()
