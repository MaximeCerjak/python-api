from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "python-backend"
    ENV: str = "dev"
    LOG_LEVEL: str = "DEBUG"

    JWT_SECRET: str = "change-me"
    JWT_ALG: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60
    API_TOKEN: str = ""

    ALLOWED_ORIGINS: List[str] = ["*"]

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
