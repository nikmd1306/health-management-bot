from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from src.keyboards.main_menu import get_main_menu
from src.database.models import User

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, user: User):
    """
    Handler for /start command.
    """
    welcome_text = (
        f"Привет, {user.full_name or message.from_user.first_name}!\n\n"
        "Я — твой медицинский ассистент. "
        "Я помогу тебе разобраться в анализах и сохранить историю здоровья.\n\n"
        "Используй меню ниже, чтобы начать."
    )
    await message.answer(welcome_text, reply_markup=get_main_menu())


@router.message(Command("help"))
async def cmd_help(message: Message):
    """
    Handler for /help command.
    """
    help_text = (
        "🚑 **Как я работаю:**\n\n"
        "1. **Анализ** — загрузи фото анализов, и я расшифрую их.\n"
        "2. **Профиль** — твои данные и настройки.\n"
        "3. **Подписка** — доступ к расширенным функциям.\n\n"
        "Если что-то пошло не так, попробуй перезапустить бота командой /start."
    )
    await message.answer(help_text, parse_mode="Markdown")
