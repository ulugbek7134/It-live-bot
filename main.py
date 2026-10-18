import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import load_config
from app.db import Database
from app.handlers import register_handlers


async def main() -> None:
    """Botni ishga tushiruvchi asosiy funksiya."""
    # Loglarni sozlash (maxfiy ma'lumotlar kiritilmaydi)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        stream=sys.stdout,
    )
    logger = logging.getLogger(__name__)

    try:
        config = load_config()
    except Exception as exc:
        logger.error("Konfiguratsiyani yuklashda xatolik: %s", exc)
        return

    # Ma'lumotlar bazasini initsializatsiya qilish
    db = Database(config.db_path)
    await db.init()
    logger.info("Ma'lumotlar bazasi muvaffaqiyatli ishga tushirildi.")

    # Bot va Dispatcher yaratish
    bot = Bot(
        token=config.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    # Baza obyektini barcha handlerlar uchun ochiq qilish
    dp["db"] = db

    # Routerlarni ulash
    register_handlers(dp)

    logger.info("Bot polling rejimida ishga tushmoqda...")
    # Kutib qolgan yangilanishlarni tozalash va pollingni boshlash
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Bot to'xtatildi.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot to'xtatildi.")
