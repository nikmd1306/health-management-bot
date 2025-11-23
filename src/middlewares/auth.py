from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User as TelegramUser
from src.database.models import User
import logging

logger = logging.getLogger(__name__)


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        telegram_user: TelegramUser = data.get("event_from_user")

        if not telegram_user:
            return await handler(event, data)

        user, created = await User.get_or_create(
            telegram_id=telegram_user.id,
            defaults={
                "username": telegram_user.username,
                "full_name": telegram_user.full_name,
            },
        )

        if not created:
            # Update user info if changed
            if (
                user.username != telegram_user.username
                or user.full_name != telegram_user.full_name
            ):
                user.username = telegram_user.username
                user.full_name = telegram_user.full_name
                await user.save()

        # Put user object into data to access it in handlers
        data["user"] = user

        if created:
            logger.info(f"New user created: {user}")

        return await handler(event, data)
