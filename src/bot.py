import asyncio
import logging
from aiogram import Bot, Dispatcher
from src.config import config
from src.logging_config import setup_logging


async def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Starting bot...")

    # Initialize Bot and Dispatcher
    bot = Bot(token=config.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()

    # Here we will include routers later
    # dp.include_router(...)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await bot.session.close()
        logger.info("Bot stopped")


if __name__ == "__main__":
    asyncio.run(main())
