from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command = 'start',
            description = 'Начало работы'
        ),
        BotCommand(
            command = 'name',
            description = 'имя'
        ),
        BotCommand(
            command='subject',
            description = 'Дисциплина'
        ),
        BotCommand(
            command='page',
            description='Балл/Посещаемость'
        ),
        BotCommand(
            command='sendphoto',
            description='Отправить мне фоточку'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())