import os
from typing import Optional

from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    postgres_db_url: str = (
        f"postgresql+asyncpg://"
        f"{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}"
        f":{os.getenv('DB_PORT')}/"
        f"{os.getenv('POSTGRES_DB')}"
    )
    sqlite_db_url: str = "sqlite+aiosqlite:///./Notes.db"
    secret: str = "VERY_SECRET_SECRET"
    ya_spellcheck_address: str = (
        "https://speller.yandex.net/services/" "spellservice.json/checkText"
    )
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="ignore"
    )


settings = Settings()
