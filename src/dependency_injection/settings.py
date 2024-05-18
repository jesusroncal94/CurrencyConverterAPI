from functools import lru_cache
from typing import Final

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


EXCHANGE_RATES_DATA_API_KEY_KEY: Final[str] = "EXCHANGE_RATES_DATA_API_KEY"
EXCHANGE_RATES_DATA_API_CURRENCY_CONVERSION_ENDPOINT_KEY: Final[str] = (
    "EXCHANGE_RATES_DATA_API_CURRENCY_CONVERSION_ENDPOINT"
)

ENV_FILE_PATH: Final[str] = ".env"

EMPTY_STRING: Final[str] = ""


class Settings(BaseSettings):
    exchange_rates_data_api_key: str
    exchange_rates_data_api_currency_conversion_endpoint: str
    postgre_sql_url: str

    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH)


@lru_cache
def get_settings() -> Settings:
    return Settings()
