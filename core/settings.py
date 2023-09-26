from decouple import config
from dataclasses import dataclass


@dataclass
class Bots:
    token: str
    admin_id: int
    provider_token: str


@dataclass
class Settings:
    bots: Bots


def get_setting():
    return Settings(
        bots=Bots(
            token=config('TOKEN'),
            admin_id=config('ADMIN_ID', cast=int),
            provider_token=config('PROVIDER_TOKEN')
        )
    )


settings = get_setting()
