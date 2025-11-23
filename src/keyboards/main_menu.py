from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_main_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="Анализ"),
        KeyboardButton(text="Профиль"),
    )
    builder.row(
        KeyboardButton(text="Подписка"),
    )

    return builder.as_markup(resize_keyboard=True)
