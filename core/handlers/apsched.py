from aiogram import Bot

from core.settings import settings


async def send_message_time(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Это сообщение отправлено через несколько секунд после старта')


async def send_message_cron(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Это сообщение будет отправлено ежедневно в указанное время')


async def send_message_interval(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Это сообщение будет отправляться с интервалом в 1 минуту')


async def send_message(bot: Bot, chat_id: int, message: str):
    await bot.send_message(chat_id, message)