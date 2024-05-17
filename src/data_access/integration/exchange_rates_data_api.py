from business_logic import Currency
from httpx import AsyncClient

from ..entities import CurrencyConversionHeaders
from ..entities import CurrencyConversionParams
from ..entities import CurrencyConversionResponse


class ExchangeRatesDataAPI:
    def __init__(self, api_key: str, currency_conversion_endpoint: str) -> None:
        self.api_key = api_key
        self.currency_conversion_endpoint = currency_conversion_endpoint

    async def get_currency_conversion(
        self, amount: float, from_currency: Currency, to_currency: Currency
    ) -> float:
        currency_conversion_headers_obj = CurrencyConversionHeaders.model_construct(
            api_key=self.api_key
        )
        currency_conversion_params_obj = CurrencyConversionParams.model_construct(
            amount=amount, from_currency=from_currency, to_currency=to_currency
        )

        async with AsyncClient() as client:
            response = await client.get(
                url=self.currency_conversion_endpoint,
                params=currency_conversion_params_obj.model_dump(by_alias=True),
                headers=currency_conversion_headers_obj.model_dump(by_alias=True),
            )
            response.raise_for_status()
            data = response.json()
            currency_conversion_response = CurrencyConversionResponse.model_validate(
                obj=data
            )

            return currency_conversion_response.result
