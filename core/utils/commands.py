from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='sendphoto',
            description='Отправить мне фоточку'
        ),
        BotCommand(
            command='stop',
            description='Закончить работу с журналом'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())