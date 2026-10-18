from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app import texts
from app.db import Database
from app.keyboards import get_main_keyboard

router = Router(name="start_router")


@router.message(CommandStart())
async def handle_start(message: Message, db: Database) -> None:
    """/start buyrug'i uchun handler."""
    user = message.from_user
    if user:
        await db.add_or_update_user(
            user_id=user.id,
            full_name=user.full_name,
            username=user.username,
        )

    name = html.quote(user.first_name if user else "Foydalanuvchi")
    await message.answer(
        text=texts.START_MESSAGE.format(name=name),
        reply_markup=get_main_keyboard(),
        parse_mode="HTML",
    )


@router.message(Command("help"))
async def handle_help_command(message: Message) -> None:
    """/help buyrug'i uchun handler."""
    await message.answer(
        text=texts.HELP_MESSAGE,
        parse_mode="HTML",
    )
