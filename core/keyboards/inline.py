from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.utils.callbackdata import MacInfo

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='MacBook Air',
            callback_data='apple_air_13_m1_2020'
        ),
    ],
    [
        InlineKeyboardButton(
            text='MacBook Pro 14',
            callback_data='apple_pro_14_m1_2020'
        ),
    ],
    [
        InlineKeyboardButton(
            text='MacBook Pro 16',
            callback_data='apple_pro_16_m1_2020'
        ),
    ],
    [
        InlineKeyboardButton(
            text='Link',
            url='https://www.apple.com/ru/shop/buy-mac/macbook-air'
        ),
    ],
    [
        InlineKeyboardButton(
            text='Profile',
            url='tg://user?id=338258059'
        ),
    ]
])


def get_inline_kb():
    kb_builder = InlineKeyboardBuilder()
    kb_builder.button(text='MacBook Air', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    kb_builder.button(text='MacBook Pro 14', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2020))
    kb_builder.button(text='MacBook Pro 16', callback_data=MacInfo(model='pro', size=16, chip='m1', year=2021))
    kb_builder.button(text='Link', url='https://www.apple.com/ru/shop/buy-mac/macbook-air')
    kb_builder.button(text='Profile', url='tg://user?id=338258059')

    kb_builder.adjust(3, 1, 1)

    return kb_builder.as_markup()
