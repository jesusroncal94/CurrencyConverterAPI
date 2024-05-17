from abc import ABC
from abc import abstractmethod

from ..domain import Currency


class CurrencyConverterRepository(ABC):
    @abstractmethod
    async def get_currency_conversion(
        self, amount: float, from_currency: Currency, to_currency: Currency
    ) -> float:
        pass
