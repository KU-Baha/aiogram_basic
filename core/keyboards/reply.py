from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ряд 1, Кнопка 1',
        ),
        KeyboardButton(
            text='Ряд 1, Кнопка 2',
        ),
        KeyboardButton(
            text='Ряд 1, Кнопка 3',
        ),
    ],
    [
        KeyboardButton(
            text='Ряд 2, Кнопка 1',
        ),
        KeyboardButton(
            text='Ряд 2, Кнопка 2',
        ),
        KeyboardButton(
            text='Ряд 2, Кнопка 3',
        ),
        KeyboardButton(
            text='Ряд 2, Кнопка 4',
        )
    ],
    [
        KeyboardButton(
            text='Ряд 3, Кнопка 1',
        ),
        KeyboardButton(
            text='Ряд 3, Кнопка 2',
        ),
    ]
],
    # resize_keyboard=True,
    one_time_keyboard=True,
    # input_field_placeholder='Выберите вариант',
    # selective=True
)

loc_tel_poll_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Отправить свою локацию',
                request_location=True
            ),
            KeyboardButton(
                text='Отправить свой контакт',
                request_contact=True
            ),
            KeyboardButton(
                text='Отправить опрос',
                request_poll=KeyboardButtonPollType(type='quiz')
            ),
            KeyboardButton(
                text='Отправить опрос (регулярный)',
                request_poll=KeyboardButtonPollType(type='regular')
            ),
        ]
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
    input_field_placeholder='Отправьте свою локацию, контакт или опрос',
)


def get_reply_kb() -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()

    kb_builder.button(text='Ряд 1, Кнопка 1')
    kb_builder.button(text='Ряд 1, Кнопка 2')
    kb_builder.button(text='Ряд 1, Кнопка 3')

    kb_builder.button(text='Геолокация', request_location=True)
    kb_builder.button(text='Контакт', request_contact=True)

    kb_builder.button(text='Опрос', request_poll=KeyboardButtonPollType(type='quiz'))
    kb_builder.button(text='Опрос (регулярный)', request_poll=KeyboardButtonPollType(type='regular'))

    kb_builder.adjust(3, 2, 2)


    return kb_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder='Выберите вариант',
    )
