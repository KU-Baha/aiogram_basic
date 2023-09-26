import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, and_f

from core.handlers.basic import get_inline, get_start, get_menu, get_test, get_location, get_photo, get_hello
from core.handlers.contact import get_true_contact, get_false_contact
from core.handlers.callback import select_macbook
from core.handlers.pay import order, pre_checkout_query, successful_payment, shipping_check
from core.filters.iscontact import IsTrueContact
from core.settings import settings
from core.utils.callbackdata import MacInfo
from core.utils.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, "Бот запущен")
    logging.info("Бот запущен")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, "Бот остановлен")
    logging.info("Бот остановлен")


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - "
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    bot = Bot(token=settings.bots.token, parse_mode='HTML')

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(order, Command("pay"))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.successful_payment)
    dp.shipping_query.register(shipping_check)

    dp.message.register(get_start, Command("start"))
    dp.message.register(get_menu, Command("menu"))
    dp.message.register(get_test, Command("test"))
    dp.message.register(get_inline, Command("inline"))

    # dp.callback_query.register(select_macbook, F.data.startswith("apple_"))
    dp.callback_query.register(select_macbook, MacInfo.filter())
    # dp.callback_query.register(select_macbook, MacInfo.filter(F.model == 'pro'))

    dp.message.register(get_location, F.location)
    dp.message.register(get_photo, F.photo)

    dp.message.register(get_hello, F.text == 'Привет')

    dp.message.register(get_true_contact, and_f(F.contact, IsTrueContact()))
    dp.message.register(get_false_contact, and_f(F.contact, ~IsTrueContact()))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
