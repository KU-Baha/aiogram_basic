import asyncio
import logging
from datetime import datetime, timedelta

import asyncpg

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, and_f
from aiogram.fsm.storage.redis import RedisStorage

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.redis import RedisJobStore

from apscheduler_di import ContextSchedulerDecorator

from core.settings import settings

from core.handlers.apsched import send_message_time, send_message_cron, send_message_interval
from core.handlers.basic import get_inline, get_start, get_menu, get_test, get_location, get_photo, get_hello
from core.handlers.contact import get_true_contact, get_false_contact
from core.handlers.callback import select_macbook
from core.handlers.pay import order, pre_checkout_query, successful_payment, shipping_check
from core.handlers import form
from core.handlers.send_media import get_audio, get_document, get_media_group, get_video, get_sticker, get_video_note, \
    get_voice

from core.filters.iscontact import IsTrueContact

from core.middlewares.work_hours import WorkHoursMiddleware
from core.middlewares.counter import CounterMiddleware
from core.middlewares.db import DbSession
from core.middlewares.apsched import SchedulerMiddleware

from core.utils.callbackdata import MacInfo
from core.utils.commands import set_commands
from core.utils.statesform import StepForm


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, "Бот запущен")
    logging.info("Бот запущен")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, "Бот остановлен")
    logging.info("Бот остановлен")


async def create_pool():
    return await asyncpg.create_pool(
        user=settings.db.user,
        password=settings.db.password,
        host=settings.db.host,
        port=settings.db.port,
        database=settings.db.database,
        command_timeout=settings.db.command_timeout
    )


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - "
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    bot = Bot(token=settings.bots.token, parse_mode='HTML')
    pool_conn = await create_pool()

    # storage = RedisStorage.from_url('redis://localhost:6379/0')

    jobstores = {
        'default': RedisJobStore(
            jobs_key='dispatched_trips_jobs',
            run_times_key='dispatched_trips_running',
            host='localhost',
            db=2,
            port=6379,
        )
    }

    dp = Dispatcher()

    scheduler = ContextSchedulerDecorator(
        AsyncIOScheduler(timezone="Asia/Bishkek", jobstores=jobstores)
    )
    scheduler.ctx.add_instance(bot, declared_class=Bot)

    # now = datetime.now()

    # scheduler.add_job(
    #     send_message_time,
    #     "date",
    #     run_date=now + timedelta(seconds=10),
    # )
    # scheduler.add_job(
    #     send_message_cron,
    #     "cron",
    #     hour=now.hour,
    #     minute=now.minute + 1,
    #     start_date=now,
    # )
    # scheduler.add_job(
    #     send_message_interval,
    #     "interval",
    #     seconds=60,
    # )
    scheduler.start()

    dp.update.middleware.register(DbSession(pool_conn))
    dp.update.middleware.register(WorkHoursMiddleware())
    dp.message.middleware.register(CounterMiddleware())
    dp.update.middleware.register(SchedulerMiddleware(scheduler))

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.successful_payment)
    dp.shipping_query.register(shipping_check)

    dp.message.register(get_audio, Command("audio"))
    dp.message.register(get_document, Command("document"))
    dp.message.register(get_media_group, Command("media_group"))
    dp.message.register(get_photo, Command("photo"))
    dp.message.register(get_video, Command("video"))
    dp.message.register(get_sticker, Command("sticker"))
    dp.message.register(get_video_note, Command("video_note"))
    dp.message.register(get_voice, Command("voice"))

    dp.message.register(form.get_form, Command("form"))
    dp.message.register(form.get_name, StepForm.GET_NAME)
    dp.message.register(form.get_last_name, StepForm.GET_LAST_NAME)
    dp.message.register(form.get_age, StepForm.GET_AGE)

    dp.message.register(order, Command("pay"))
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
