from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardMarkup, InlineKeyboardButton, \
    ShippingOption, ShippingQuery

from core.settings import settings

keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оплатить', pay=True)
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='cancel')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

KG_SHIPPING = ShippingOption(
    id='kg',
    title='Доставка в Кыргызстан',
    prices=[
        LabeledPrice(
            label='Доставка со SDEK',
            amount=300
        ),
    ]
)

RU_SHIPPING = ShippingOption(
    id='ru',
    title='Доставка в Россию',
    prices=[
        LabeledPrice(
            label='Доставка со SDEK',
            amount=700
        ),
    ]
)

KZ_SHIPPING = ShippingOption(
    id='kz',
    title='Доставка в Казахстан',
    prices=[
        LabeledPrice(
            label='Доставка со SDEK',
            amount=500
        ),
    ]
)

CITIES_SHIPPING = ShippingOption(
    id='cities',
    title='Доставка по городам',
    prices=[
        LabeledPrice(
            label='Доставка со SDEK',
            amount=100
        ),
    ]
)


async def shipping_check(shipping_query: ShippingQuery, bot: Bot):
    shipping_options = []
    countries = ['KG', 'RU', 'KZ']

    if shipping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(
            shipping_query_id=shipping_query.id,
            ok=False,
            error_message='Доставка в вашу страну не осуществляется'
        )

    if shipping_query.shipping_address.country_code == 'KG':
        shipping_options.append(KG_SHIPPING)

    elif shipping_query.shipping_address.country_code == 'RU':
        shipping_options.append(RU_SHIPPING)

    elif shipping_query.shipping_address.country_code == 'KZ':
        shipping_options.append(KZ_SHIPPING)

    cities = ['Бишкек', 'Ош', 'Алматы', 'Нур-Султан']

    if shipping_query.shipping_address.city in cities:
        shipping_options.append(CITIES_SHIPPING)

    await bot.answer_shipping_query(
        shipping_query_id=shipping_query.id,
        ok=True,
        shipping_options=shipping_options
    )


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Покупка через бота',
        description='Покупка через бота',
        payload='Payment through the bot',
        provider_token=settings.bots.provider_token,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Доступ к секретной информации',
                amount=100000
            ),
            LabeledPrice(
                label='НДС',
                amount=20000
            ),
            LabeledPrice(
                label='Скидка',
                amount=-15000
            ),
            LabeledPrice(
                label='Бонус',
                amount=-5000
            )
        ],
        max_tip_amount=5000,  # Максимальная сумма чаевых
        suggested_tip_amounts=[1000, 2000, 3000, 4000],  # Суммы чаевых
        start_parameter='dataxway',
        provider_data=None,  # Данные провайдера
        photo_url='https://docs.python-telegram-bot.org/en/v20.5/_static/ptb-logo_1024.png',  # URL фото
        # photo_size=512,  # Размер фото в байтах
        photo_width=512,  # Ширина фото
        photo_height=512,  # Высота фото
        need_name=False,  # Запрашивать имя
        need_phone_number=False,  # Запрашивать номер телефона
        need_email=False,  # Запрашивать email
        need_shipping_address=True,  # Запрашивать адрес доставки
        send_phone_number_to_provider=False,  # Отправлять номер телефона провайдеру
        send_email_to_provider=False,  # Отправлять email провайдеру
        is_flexible=True,  # Гибкая цена
        disable_notification=False,  # Отключить уведомления
        protect_content=False,  # Защитить контент
        reply_to_message_id=None,  # Ответить на сообщение
        allow_sending_without_reply=True,  # Разрешить отправку без ответа
        reply_markup=keyboards,  # Клавиатура (Первой кнопкой должен быть Pay)
        request_timeout=15  # Таймаут запроса
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(
        pre_checkout_query_id=pre_checkout_query.id,
        ok=True,
        error_message='Ошибка при оплате'
    )


async def successful_payment(message: Message):
    msg = (f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.'
           f'\r\nНаш менеджер свяжется с вами в ближайшее время')
    await message.answer(msg)
