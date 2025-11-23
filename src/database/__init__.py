from tortoise import Tortoise
import logging
from src.config import TORTOISE_ORM

logger = logging.getLogger(__name__)


async def init_db():
    """
    Инициализация подключения к базе данных.
    """
    logger.info("Initializing database connection...")
    try:
        await Tortoise.init(config=TORTOISE_ORM)
        logger.info("Database connection initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


async def close_db():
    """
    Закрытие подключения к базе данных.
    """
    logger.info("Closing database connection...")
    await Tortoise.close_connections()
    logger.info("Database connection closed.")
