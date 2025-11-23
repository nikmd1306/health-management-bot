from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from src.states import OnboardingSG
from src.database.models import User
from src.keyboards.main_menu import get_main_menu

router = Router()


@router.message(Command("onboarding"))
@router.message(StateFilter(None), F.text == "Заполнить анкету")
async def start_onboarding_manual(message: Message, state: FSMContext):
    await start_onboarding(message, state)


async def start_onboarding(message: Message, state: FSMContext):
    """
    Запуск сценария анкетирования.
    """
    await state.set_state(OnboardingSG.age)

    # AICODE-TODO: Добавить кнопку "Отмена" или команду /cancel для выхода из FSM
    await message.answer(
        "Давай заполним твой профиль, чтобы я мог давать более точные рекомендации.\n\n"
        "Сколько тебе лет?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(OnboardingSG.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введи возраст числом (например, 30).")
        return

    age = int(message.text)
    if not (0 < age < 120):
        await message.answer("Пожалуйста, укажи реальный возраст.")
        return

    await state.update_data(age=age)
    await state.set_state(OnboardingSG.gender)

    # Клавиатура для выбора пола
    gender_kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Мужской"), KeyboardButton(text="Женский")]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await message.answer("Твой пол?", reply_markup=gender_kb)


@router.message(OnboardingSG.gender)
async def process_gender(message: Message, state: FSMContext):
    gender = message.text
    if gender not in ["Мужской", "Женский"]:
        await message.answer("Пожалуйста, выбери пол, используя кнопки ниже.")
        return

    await state.update_data(gender=gender)
    await state.set_state(OnboardingSG.context)

    await message.answer(
        "Есть ли у тебя какие-то хронические заболевания или жалобы, "
        "о которых мне стоит знать?\n"
        "(Напиши 'Нет', если ничего не беспокоит)",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(OnboardingSG.context)
async def process_context(message: Message, state: FSMContext, user: User):
    complaints = message.text
    # AICODE-TODO: Добавить лимит на длину текста (например, 1000 символов)

    data = await state.get_data()

    # Сохранение данных в БД
    user.age = data["age"]
    user.gender = data["gender"]
    user.complaints = complaints
    await user.save()

    await state.clear()

    await message.answer(
        "Спасибо! Данные сохранены.\n"
        "Теперь ты можешь отправить мне фото анализов для расшифровки.",
        reply_markup=get_main_menu(),
    )
