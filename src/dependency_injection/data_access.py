from typing import Annotated

from business_logic import CurrencyConverterRepository
from data_access import CurrencyConverterRepositoryImplemented
from data_access import ExchangeRatesDataAPI
from fastapi import Depends

from .settings import get_settings
from .settings import Settings


def get_exchange_rates_data_api(
    settings: Annotated[Settings, Depends(dependency=get_settings)],
) -> ExchangeRatesDataAPI:
    return ExchangeRatesDataAPI(
        api_key=settings.exchange_rates_data_api_key,
        currency_conversion_endpoint=settings.exchange_rates_data_api_currency_conversion_endpoint,
    )


def get_currency_converter_repository(
    exchange_rates_data_api: ExchangeRatesDataAPI = Depends(
        dependency=get_exchange_rates_data_api
    ),
) -> CurrencyConverterRepository:
    return CurrencyConverterRepositoryImplemented(
        exchange_rates_data_api=exchange_rates_data_api
    )
