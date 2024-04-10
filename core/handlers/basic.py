from aiogram import Bot
from aiogram.types import Message

async def get_start(message: Message, bot: Bot):
    await message.answer(f'<tg-spoiler>Привет {message.from_user.first_name}. Рад тебя видеть!!</tg-spoiler>')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично. Теперь твоя фотка в моих сохраненках_-_')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')