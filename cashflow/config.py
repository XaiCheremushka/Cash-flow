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

    # Database
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: SecretStr
    DATABASE_HOST: str
    DATABASE_PORT: str

    # JWT
    ACCESS_TOKEN_LIFETIME: timedelta
    REFRESH_TOKEN_LIFETIME: timedelta
    ALGORITHM: str
    AUTH_HEADER_TYPE: str

    @field_validator("ACCESS_TOKEN_LIFETIME", "REFRESH_TOKEN_LIFETIME", mode='before')
    def parse_timedelta(cls, value):
        """Конвертация значения из минут в timedelta."""
        return timedelta(minutes=int(value))


conf = Settings()