import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_user(self, user_id, username):
        query = f"INSERT INTO users (user_id, username) VALUES ({user_id}, '{username}') " \
                f"ON CONFLICT (user_id) DO UPDATE SET username = '{username}'"
        await self.connector.execute(query)
