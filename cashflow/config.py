from pydantic_settings import BaseSettings
from pydantic import SecretStr, field_validator
from datetime import timedelta

class Settings(BaseSettings):
    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"

    # Project
    SECRET_KEY: SecretStr
    ALLOWED_HOSTS: SecretStr
    SITE_HOST: str
    SITE_PORT: str

    # Database
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: SecretStr
    DATABASE_HOST: str = 'postgres'
    DATABASE_PORT: str = '5432'

    # PgAdmin
    PGADMIN_DEFAULT_EMAIL: str
    PGADMIN_DEFAULT_PASSWORD: SecretStr

    # JWT
    # ACCESS_TOKEN_LIFETIME: timedelta
    # REFRESH_TOKEN_LIFETIME: timedelta
    # ALGORITHM: str
    # AUTH_HEADER_TYPE: str
    #
    # @field_validator("ACCESS_TOKEN_LIFETIME", "REFRESH_TOKEN_LIFETIME", mode='before')
    # def parse_timedelta(cls, value):
    #     """Конвертация значения из минут в timedelta."""
    #     return timedelta(minutes=int(value))


conf = Settings()