from aiogram.fsm.state import State, StatesGroup


class RegistrationState(StatesGroup):
    """Foydalanuvchini ro'yxatga olish holatlari (namuna)."""
    waiting_for_name = State()
    waiting_for_phone = State()
