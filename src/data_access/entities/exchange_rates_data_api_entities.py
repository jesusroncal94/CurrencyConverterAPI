from typing import Final

from business_logic import Currency
from pydantic import BaseModel
from pydantic import Field
from pydantic import field_serializer


AMOUNT_FIELD: Final[str] = "amount"
FROM_CURRENCY_FIELD: Final[str] = "from"
TO_CURRENCY_FIELD: Final[str] = "to"

API_KEY_FIELD: Final[str] = "apikey"

RESULT_FIELD: Final[str] = "result"


class CurrencyConversionParams(BaseModel):
    amount: float = Field(alias=AMOUNT_FIELD)
    from_currency: Currency = Field(alias=FROM_CURRENCY_FIELD)
    to_currency: Currency = Field(alias=TO_CURRENCY_FIELD)

    @field_serializer("from_currency")
    def serialize_from_currency(self, from_currency: Currency, _info):
        return from_currency.value

    @field_serializer("to_currency")
    def serialize_to_currency(self, to_currency: Currency, _info):
        return to_currency.value


class CurrencyConversionHeaders(BaseModel):
    api_key: str = Field(alias=API_KEY_FIELD)


class CurrencyConversionResponse(BaseModel):
    result: float = Field(alias=RESULT_FIELD)
