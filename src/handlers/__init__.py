from aiogram import Router
from .base import router as base_router

# Main router that will include all other routers
router = Router()

router.include_router(base_router)
