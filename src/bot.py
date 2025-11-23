import asyncio
import logging
from aiogram import Bot, Dispatcher
from src.config import config
from src.logging_config import setup_logging
from src.database import init_db, close_db
from src.middlewares.auth import AuthMiddleware
from src.handlers import router as main_router


async def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Starting bot...")

    # Initialize Bot and Dispatcher
    bot = Bot(token=config.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()

    # Setup Middleware
    # Register AuthMiddleware for messages and callback queries
    # We use outer_middleware to ensure user exists before filters and handlers run
    dp.message.outer_middleware(AuthMiddleware())
    dp.callback_query.outer_middleware(AuthMiddleware())

    # Include Routers
    dp.include_router(main_router)

    try:
        await init_db()
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await close_db()
        await bot.session.close()
        logger.info("Bot stopped")


if __name__ == "__main__":
    asyncio.run(main())
