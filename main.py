import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from yt_dlp import YoutubeDL

TOKEN = "8503214446:AAFPs6rs_PXEsl7JkUyuEUAkGxua1TvqEg0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def download_video(url):
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'max_filesize': 48 * 1024 * 1024,
    }
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # ReplyKeyboardRemove tugmalarni o'chirib tashlaydi
    await message.answer(
        "Salom! Menga faqat link yuboring (Insta, TikTok, YT).",
        reply_markup=ReplyKeyboardRemove()
    )

@dp.message(F.text.startswith("http"))
async def handle_link(message: types.Message):
    status_msg = await message.answer("⏳ Yuklanmoqda...")
    try:
        file_path = download_video(message.text)
        video = types.FSInputFile(file_path)
        await message.answer_video(video=video, caption="✅ Tayyor!")
        await status_msg.delete()
        
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception:
        await status_msg.edit_text("❌ Xatolik: Video yuklanmadi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
