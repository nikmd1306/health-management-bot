from aiogram import Router
from .base import router as base_router
from .onboarding import router as onboarding_router

# Main router that will include all other routers
router = Router()

router.include_router(onboarding_router)
router.include_router(base_router)
