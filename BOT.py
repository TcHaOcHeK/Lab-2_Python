import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo
import asyncio
from aiogram.filters import Command, CommandStart
token = '7064100380:AAEmYNxYe0s0aBlO2YpbpaL3fnBP99CNmv0'



async  def start_bot(bot: Bot):
    await bot.send_message(1024576085, text= 'Бот в ахуи!!!')


async def stop_bot(bot: Bot):
    await bot.send_message(1024576085, text='Бот в трихуи!!!')


async def start():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token = token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

def GO():
    asyncio.run(start())