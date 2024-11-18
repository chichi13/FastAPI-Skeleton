from enum import Enum

from pydantic_settings import BaseSettings


class AppEnvironment(str, Enum):
    PRODUCTION = "production"
    DEV = "development"
    TESTING = "testing"


class Config(BaseSettings):
    """
    Base configuration.
    """

    API_V1_STR: str = "/api/v1"

    APP_VERSION: str = "Unversioned API"
    ENV: AppEnvironment = AppEnvironment.PRODUCTION

    UVICORN_HOST: str = "0.0.0.0"
    UVICORN_PORT: int = 8000

    BACKEND_CORS_ORIGINS: str = ""
    PROJECT_NAME: str | None = "FastAPI app template"

    SENTRY_ENABLED: bool | None = False
    SENTRY_DSN: str | None = ""
    SENTRY_ENV: str | None = "dev"

    DATABASE_USER: str = "app"
    DATABASE_PASSWORD: str = "password"
    DATABASE_URL: str = "127.0.0.1"
    DATABASE_NAME: str = "app"
    DATABASE_PORT: int = 5432
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10

    LOGGING_LEVEL: str = "INFO"
    SQL_VERBOSE_LOGGING: bool = False

    def is_dev(self) -> bool:
        return self.ENV == AppEnvironment.DEV

    def is_prod(self) -> bool:
        return self.ENV == AppEnvironment.PRODUCTION


settings = Config(_env_file=".env", _env_file_encoding="utf-8")
