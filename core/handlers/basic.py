from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard
import time
admin = 1024576085

async def get_start(message: Message, bot: Bot):
    await message.answer(f'<tg-spoiler>Привет {message.from_user.first_name}. Рад тебя видеть!!</tg-spoiler>',
                         reply_markup=reply_keyboard)

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично. Теперь твоя фотка в моих сохраненках_-_')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.send_message(admin, text='фоточки подъехали')
    await bot.download_file(file.file_path, 'fileSave/photo{}.jpg'.format(time.time()))