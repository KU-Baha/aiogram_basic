from typing import Callable, Awaitable, Dict, Any

import asyncpg.pool
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from core.utils.db import Request


class DbSession(BaseMiddleware):
    def __init__(self, connector: asyncpg.pool.Pool) -> None:
        super().__init__()
        self.connector = connector

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        async with self.connector.acquire() as conn:
            data['request'] = Request(conn)
            return await handler(event, data)
