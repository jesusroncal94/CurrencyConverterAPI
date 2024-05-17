from business_logic import Currency
from business_logic import CurrencyConverterRepository

from ..integration import ExchangeRatesDataAPI


class CurrencyConverterRepositoryImplemented(CurrencyConverterRepository):
    def __init__(self, exchange_rates_data_api: ExchangeRatesDataAPI) -> None:
        self.exchange_rates_data_api = exchange_rates_data_api

    async def get_currency_conversion(
        self, amount: float, from_currency: Currency, to_currency: Currency
    ) -> float:
        return await self.exchange_rates_data_api.get_currency_conversion(
            amount=amount, from_currency=from_currency, to_currency=to_currency
        )
