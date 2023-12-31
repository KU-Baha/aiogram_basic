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
        BotCommand(
            command="audio",
            description="Аудио"
        ),
        BotCommand(
            command="document",
            description="Документ"
        ),
        BotCommand(
            command="media_group",
            description="Медиа группа"
        ),
        BotCommand(
            command="photo",
            description="Фото"
        ),
        BotCommand(
            command="sticker",
            description="Стикер"
        ),
        BotCommand(
            command="video",
            description="Видео"
        ),
        BotCommand(
            command="video_note",
            description="Видео заметка"
        ),
        BotCommand(
            command="voice",
            description="Голосовое сообщение"
        ),
    ]

    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
