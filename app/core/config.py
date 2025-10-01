from pydantic_settings import BaseSettings, SettingsConfigDict

from typing import Annotated, Any, Literal

from pydantic import (
    AnyUrl,
    BeforeValidator,
    EmailStr,
    HttpUrl,
    PostgresDsn,
    computed_field,
    model_validator,
)

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file='../.env',
        ignored_types=True
    )
# Sqlite config
    sqlite_filename = 'database.db'
    sqlite_url = f'sqlite:///{sqlite_filename}'

    connect_args = {'check_same_thread': False}

# Postres config
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""

    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
    

settings = Settings()