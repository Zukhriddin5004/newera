from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # PROJECT INFO
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    PROJECT_VERSION: str

    # POSTGRES CREDENTIALS
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    JWT_SECRET_KEY: str
    JWT_EXPIRE_SECONDS: int
    JWT_ENCRYPT_ALGORITHM: str

    model_config = SettingsConfigDict(env_file='.env')


@cache
def get_settings() -> Settings:
    return Settings()
