from ..domain import Currency
from ..repositories import CurrencyConverterRepository


class CurrencyConverterService:
    def __init__(self, currency_converter_repository: CurrencyConverterRepository):
        self.currency_converter_repository = currency_converter_repository

    async def convert_currency(
        self, amount: float, from_currency: Currency, to_currency: Currency
    ) -> float:
        currency_conversion = (
            await self.currency_converter_repository.get_currency_conversion(
                amount=amount, from_currency=from_currency, to_currency=to_currency
            )
        )
        return currency_conversion
