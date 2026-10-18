from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from app import texts


def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Asosiy menyu klaviaturasini qaytaradi."""
    kb = [
        [
            KeyboardButton(text=texts.BTN_HELP),
            KeyboardButton(text=texts.BTN_CONTACT),
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
