"""Application configuration class."""

from pydantic_settings import BaseSettings

__all__ = ("app_config", )


class AppConfig(BaseSettings):
    """Main class that holds application configuration read from environment variables."""
    bot_token: str


app_config = AppConfig()
