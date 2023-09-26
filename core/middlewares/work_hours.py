from datetime import datetime

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from typing import Callable, Awaitable, Dict, Any


def work_hours() -> bool:
    return datetime.now().weekday() in (0, 1, 2, 3, 4) and datetime.now().hour in range(9, 23)


class WorkHoursMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if not work_hours():
            return await event.answer(f'Время работы бота с 9 до 18 по будням. Сейчас {datetime.now()}')

        return await handler(event, data)
