from aiogram.fsm.state import State, StatesGroup


class OnboardingSG(StatesGroup):
    age = State()
    gender = State()
    context = State()
