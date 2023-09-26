from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Начать работу"
        ),
        BotCommand(
            command="menu",
            description="Меню"
        ),
        BotCommand(
            command="cancel",
            description="Отмена"
        ),
        BotCommand(
            command="inline",
            description="Тест"
        ),
        BotCommand(
            command="pay",
            description="Оплата"
        ),
        BotCommand(
            command="form",
            description="Форма"
        ),
    ]

    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
