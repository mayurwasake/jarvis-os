from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application configuration.

    Every module in JARVIS OS gets its configuration
    from this class.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --------------------------------------------------
    # Application
    # --------------------------------------------------

    app_name: str = Field(
        default="JARVIS OS",
        description="Application name",
    )

    version: str = Field(
        default="0.1.0",
    )

    environment: str = Field(
        default="development",
    )

    debug: bool = Field(
        default=True,
    )

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    log_level: str = Field(
        default="INFO",
    )

    # --------------------------------------------------
    # API
    # --------------------------------------------------

    host: str = Field(
        default="127.0.0.1",
    )

    port: int = Field(
        default=8000,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a singleton Settings object.
    """
    return Settings()


settings = get_settings()