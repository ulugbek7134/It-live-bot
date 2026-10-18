# Telegram Bot Loyihasi — Agent Qoidalari va Ko'rsatmalari

## OLTIN QOIDA (HAR DOIM AMAL QILINADI)
Har safar bot kodiga, sozlamalariga, matnlariga yoki loyiha fayllariga biron bir o'zgartirish kiritilsa:
1. O'zgarishlar **AVTOMATIK TARZDA GITHUB'GA** (`ulugbek7134/It-live-bot`, `main` tarmog'iga) yuklanishi shart!
2. Railway ushbu GitHub repozitoriyga ulangan, shu sababli GitHub'ga yuklanishi bilan Railway bulutidagi bot ham 24/7 rejimda avtomatik yangilanadi.
3. Maxfiylik qat'iy saqlanadi: `.env`, tokenlar, ma'lumotlar bazasi (`data/*.db`) hech qachon GitHub'ga yuklanmaydi.

---

## Qat'iy Qoidalar:
1. **Maxfiylik:** `BOT_TOKEN` va boshqa sirlarni hech qachon kodga, chatga yoki log'ga chiqarma. Faqat `.env`.
2. **Git ignore:** `.env`, `.venv`, `data/`, `*.db` — har doim `.gitignore`'da bo'lishi shart.
3. **Ruxsat:** Fayl o'chirish yoki katta o'zgarishdan oldin nima qilishingni ayt va ruxsat so'ra.
4. **Sinov:** Har bosqichdan keyin yangilanishni tekshir va Telegram'da nimani sinashni foydalanuvchiga tushuntir.
5. **Xatolar tahlili:** Xato chiqsa — avval sababini tushuntir, keyin minimal tuzatish qil.
6. **Til:** Barcha javoblar, izohlar va xabarlar o'zbek tilida.

---

## Loyiha Texnologiyalari va Ma'lumotlari:
- **Python:** 3.12, aiogram 3 (eng so'nggi 3.x), aiosqlite, python-dotenv
- **Baza:** SQLite, DB_PATH muhit o'zgaruvchisidan (standart: `data/bot.db`)
- **Deploy:** Railway (GitHub orqali 24/7 bulutda, Persistent Volume `/app/data`)
- **GitHub Repozitoriy:** `https://github.com/ulugbek7134/It-live-bot` (Branch: `main`)
- **Telegram Bot:** `@oknoline_uz_bot`
