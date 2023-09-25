from aiogram import Bot
from aiogram.types import Message


async def get_true_contact(message: Message, bot: Bot, phone_number: str):
    await message.answer(f'Ты отправил свой контакт, {phone_number}')


async def get_false_contact(message: Message, bot: Bot):
    await message.answer(f'Ты отправил не свой контакт!')
