import time

from aiogram import Bot
from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMedia, InputMediaVideo
from aiogram.utils.chat_action import ChatActionSender


async def get_audio(message: Message, bot: Bot):
    audio = FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/music.mp3')
    await bot.send_audio(message.chat.id, audio, caption='Это аудио сообщение')


async def get_document(message: Message, bot: Bot):
    document = FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/Bot Test Document.pdf', filename='BotDocument.pdf')
    await bot.send_document(message.chat.id, document, caption='Это документ')


async def get_media_group(message: Message, bot: Bot):
    async with ChatActionSender(bot=bot, chat_id=message.chat.id, action='upload_photo'):
        photo1_mg = InputMediaPhoto(
            type='photo',
            media=FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/Bot Test Photo 1.png'),
        )
        photo2_mg = InputMediaPhoto(
            type='photo',
            media=FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/Bot Test Photo 2.jpeg'),
        )
        video_mg = InputMediaVideo(
            type='video',
            media=FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/Bot Test Video Note.mp4', filename='BotVideo.mp4'),
        )
        media = [
            photo1_mg,
            photo2_mg,
            video_mg
        ]
        await bot.send_media_group(message.chat.id, media=media)


async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/Bot Test Photo 1.png', filename='BotPhoto1.jpg')
    await bot.send_photo(message.chat.id, photo, caption='Это фото')


async def get_sticker(message: Message, bot: Bot):
    sticker = FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/Bot Test Sticker.webp', filename='BotSticker.webp')
    await bot.send_sticker(message.chat.id, sticker)


async def get_video(message: Message, bot: Bot):
    async with ChatActionSender(bot=bot, chat_id=message.chat.id, action='upload_video'):
        video = FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/Bot Test Video.mp4')
        await bot.send_video(message.chat.id, video)


async def get_video_note(message: Message, bot: Bot):
    async with ChatActionSender(bot=bot, chat_id=message.chat.id, action='upload_video_note'):
        video_note = FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/Bot Test Video Note.mp4')
        await bot.send_video_note(message.chat.id, video_note)


async def get_voice(message: Message, bot: Bot):
    async with ChatActionSender(bot=bot, chat_id=message.chat.id, action='upload_voice'):
        voice = FSInputFile('/Users/baha/Desktop/Work/tg_bot/media/Bot Test Voice.m4a', filename='BotVoice.mp3')
        await bot.send_voice(message.chat.id, voice, caption='Это голосовое сообщение')
