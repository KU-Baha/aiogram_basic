from decouple import config
from dataclasses import dataclass


@dataclass
class Bots:
    token: str
    admin_id: int
    provider_token: str


@dataclass
class DB:
    user: str
    password: str
    database: str
    host: str
    port: str
    command_timeout: int = 60


@dataclass
class Settings:
    bots: Bots
    db: DB


def get_setting():
    return Settings(
        bots=Bots(
            token=config('TOKEN'),
            admin_id=config('ADMIN_ID', cast=int),
            provider_token=config('PROVIDER_TOKEN')
        ),
        db=DB(
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            database=config('DB_NAME'),
            host=config('DB_HOST'),
            port=config('DB_PORT'),
            command_timeout=config('DB_COMMAND_TIMEOUT', cast=int)
        )
    )


settings = get_setting()
