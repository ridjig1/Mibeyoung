import asyncio
from telethon.sync import TelegramClient

BOT_TOKEN = "7974182257:AAHApOGYb-ao7zKtg7AvaaZ0kNXpqJFRJq8"
CHAT_ID  = -1003258810345   # канал «Заказы👗»

async def main():
    async with TelegramClient("mi_session", 6, "eb06d4abfb49dc3eeb1aeb98ae0f581e").start(bot_token=BOT_TOKEN) as client:
        await client.send_message(
            CHAT_ID,
            "🔔 Нове замовлення #TEST\n"
            "Ім’я: Олена Кравчук\n"
            "Тел: +380671234567\n"
            "Сума: 420 $ / 15 960 ₴\n"
            "Товари:\n"
            "1. «Aurora» 44 розмір ×1  380 $\n"
            "2. «Silk Mini» 42 розмір ×1  40 $ (sale)",
        )
        print("✅ Тестовое уведомление отправлено в канал «Заказы👗»")

if __name__ == "__main__":
    asyncio.run(main())