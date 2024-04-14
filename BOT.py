import logging

import dp
from aiogram import Bot, Dispatcher, F
import asyncio

from core.handlers.basic import get_start, get_photo, Subject, Page, get_name, send_photo
from aiogram.filters import Command, CommandStart
from core.utils.commands import set_commands
from core.handlers.callback import select_subject, select_page, db_read, db_read_only_grate
from core.utils.states import Send

token = '7064100380:AAEmYNxYe0s0aBlO2YpbpaL3fnBP99CNmv0'
admin = 1024576085
eww = ''


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(admin, text='Бот активен')


async def stop_bot(bot: Bot):
    await bot.send_message(admin, text='Бот выключен')


async def start():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token = token, parse_mode = 'HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, CommandStart())

    dp.message.register(send_photo, Command(commands='sendphoto'))
    dp.message.register(get_photo, Send.photo, F.photo)

    dp.message.register(Subject, Command(commands='subject'))
    dp.callback_query.register(db_read, F.data.startswith('subject_'))

    dp.message.register(Page, Send.name)
    dp.callback_query.register(db_read_only_grate, F.data.startswith('page_'))
    dp.message.register(get_name, Command(commands='name'))





    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


def GO():
    asyncio.run(start())
