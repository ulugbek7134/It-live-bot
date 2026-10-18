from aiogram import F, Router
from aiogram.types import Message
from app import texts

router = Router(name="common_router")


@router.message(F.text == texts.BTN_HELP)
async def handle_help_button(message: Message) -> None:
    """Yordam tugmasi uchun handler."""
    await message.answer(
        text=texts.HELP_MESSAGE,
        parse_mode="HTML",
    )


@router.message(F.text == texts.BTN_CONTACT)
async def handle_contact_button(message: Message) -> None:
    """Aloqa tugmasi uchun handler."""
    await message.answer(
        text="Savol va takliflar uchun: @admin bilan bog'lanishingiz mumkin.",
    )


@router.message(F.text)
async def handle_other_text(message: Message) -> None:
    """Noma'lum matnli xabarlar uchun handler."""
    await message.answer(
        text=texts.UNKNOWN_COMMAND,
    )
