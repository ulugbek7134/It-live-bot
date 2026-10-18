import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()


@dataclass(frozen=True)
class Config:
    """Ilova konfiguratsiyasi."""
    bot_token: str
    db_path: str


def load_config() -> Config:
    """Muhit o'zgaruvchilarini yuklaydi va tekshiradi."""
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token or token == "your_bot_token_here":
        raise ValueError(
            "Xatolik: BOT_TOKEN topilmadi yoki noto'g'ri ko'rsatilgan. "
            "Iltimos, .env faylida BOT_TOKEN ni to'g'ri kiriting."
        )

    db_path = os.getenv("DB_PATH", "data/bot.db").strip()
    if not db_path:
        db_path = "data/bot.db"

    # Ma'lumotlar bazasi papkasi mavjud bo'lmasa, yaratib qo'yish
    db_file = Path(db_path)
    db_file.parent.mkdir(parents=True, exist_ok=True)

    return Config(
        bot_token=token,
        db_path=db_path,
    )
