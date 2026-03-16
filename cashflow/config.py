from pydantic_settings import BaseSettings
from pydantic import SecretStr

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

conf = Settings()