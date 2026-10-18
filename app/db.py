from datetime import datetime
from typing import Optional
import aiosqlite


class Database:
    """SQLite bilan asinxron ishlash klassi."""

    def __init__(self, db_path: str):
        self.db_path = db_path

    async def init(self) -> None:
        """Baza jadvallarini yaratish va sozlash."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    full_name TEXT NOT NULL,
                    username TEXT,
                    created_at TEXT NOT NULL
                )
            """)
            await db.commit()

    async def add_or_update_user(
        self, user_id: int, full_name: str, username: Optional[str]
    ) -> None:
        """Foydalanuvchini bazaga qo'shish yoki ma'lumotlarini yangilash."""
        now = datetime.now().isoformat()
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO users (user_id, full_name, username, created_at)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    full_name=excluded.full_name,
                    username=excluded.username
            """, (user_id, full_name, username, now))
            await db.commit()

    async def get_user(self, user_id: int) -> Optional[dict]:
        """Foydalanuvchini user_id bo'yicha olish."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT user_id, full_name, username, created_at FROM users WHERE user_id = ?",
                (user_id,),
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    return dict(row)
                return None

    async def get_users_count(self) -> int:
        """Jami foydalanuvchilar soni."""
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute("SELECT COUNT(*) FROM users") as cursor:
                row = await cursor.fetchone()
                return row[0] if row else 0
