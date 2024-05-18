from typing import Annotated

from business_logic import CurrencyConverterRepository
from business_logic import CurrencyConverterService
from business_logic import UserRegisterService
from fastapi import Depends

from .data_access import get_currency_converter_repository
from .data_access import get_user_repository


def get_currency_converter_service(
    currency_converter_repository: Annotated[
        CurrencyConverterRepository,
        Depends(dependency=get_currency_converter_repository),
    ],
) -> CurrencyConverterService:
    return CurrencyConverterService(
        currency_converter_repository=currency_converter_repository
    )


def get_user_register_service(
    user_repository: Annotated[
        CurrencyConverterRepository, Depends(dependency=get_user_repository)
    ],
) -> UserRegisterService:
    return UserRegisterService(user_repository=user_repository)
