import json

from aiogram import Bot
from aiogram.types import Message

from core.keyboards.reply import reply_kb, loc_tel_poll_kb, get_reply_kb
from core.keyboards.inline import select_macbook, get_inline_kb


async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.full_name}!'
                         f'Выбери модель MacBook',
                         reply_markup=get_inline_kb())


async def get_start(message: Message, bot: Bot):
    # await bot.send_message(message.chat.id, f'Привет, {message.from_user.full_name}!')
    # await message.reply('Для начала работы введи команду /start')
    await message.answer(f'Привет, {message.from_user.full_name}!',
                         reply_markup=reply_kb)


async def get_menu(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.full_name}!',
                         reply_markup=loc_tel_poll_kb)


async def get_test(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.full_name}!',
                         reply_markup=get_reply_kb())


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Отлично. Ты отправил мне свою геолокацию, {message.from_user.full_name}!'
                         f'Координаты: {message.location.latitude}, {message.location.longitude}')


async def get_photo(message: Message, bot: Bot):
    await message.answer('Отлично. Ты отправил картинку, я сохраню ее себе.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, f"files/{file.file_unique_id}.jpg")


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    json_str = json.dumps(message.model_dump(), default=str)
