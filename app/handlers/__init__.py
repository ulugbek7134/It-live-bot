from aiogram import Dispatcher
from app.handlers.start import router as start_router
from app.handlers.common import router as common_router


def register_handlers(dp: Dispatcher) -> None:
    """Barcha routerlarni dispatcherga ro'yxatga oladi."""
    dp.include_router(start_router)
    dp.include_router(common_router)
