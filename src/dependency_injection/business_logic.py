from business_logic import CurrencyConverterRepository
from business_logic import CurrencyConverterService
from fastapi import Depends

from .data_access import get_currency_converter_repository


def get_currency_converter_service(
    currency_converter_repository: CurrencyConverterRepository = Depends(
        dependency=get_currency_converter_repository
    ),
) -> CurrencyConverterService:
    return CurrencyConverterService(
        currency_converter_repository=currency_converter_repository
    )
