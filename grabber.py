import asyncio, json, os, re
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from PIL import Image
import aiofiles

API_ID   = 6                                    # публичный layer, работает всегда
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e" # тот же публичный
BOT_TOKEN = "7974182257:AAHApOGYb-ao7zKtg7AvaaZ0kNXpqJFRJq8"
CHAT_ID  = -1003083328965                      # канал товаров
OUT_DIR  = "seed"

def to_webp(src, dst, max_side=1800):
    img = Image.open(src)
    img.thumbnail((max_side, max_side), Image.LANCZOS)
    img.save(dst, "WEBP", quality=90)

async def main():
    os.makedirs(f"{OUT_DIR}/media", exist_ok=True)
    async with TelegramClient("mi_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN) as client:
        messages = []
        async for msg in client.iter_messages(CHAT_ID, reverse=True):
            if not msg.media: continue
            row = {"id": msg.id, "text": msg.text or "", "photos": [], "video": None}
            if isinstance(msg.media, MessageMediaPhoto):
                fname = f"{OUT_DIR}/media/{msg.id}_photo.jpg"
                await msg.download_media(fname)
                webp = fname.replace(".jpg", ".webp")
                to_webp(fname, webp)
                row["photos"].append(os.path.basename(webp))
            elif isinstance(msg.media, MessageMediaDocument) and msg.video:
                fname = f"{OUT_DIR}/media/{msg.id}_video.mp4"
                await msg.download_media(fname)
                row["video"] = os.path.basename(fname)
            messages.append(row)
        with open(f"{OUT_DIR}/raw.json", "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        print(f"✅ Скачано {len(messages)} постов в {OUT_DIR}")

if __name__ == "__main__":
    asyncio.run(main())