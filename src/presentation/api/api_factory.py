from typing import Final

from fastapi import FastAPI

from .routes.currency_conversion import convert_currency_endpoint


API_PREFIX: Final[str] = "/api/v1"
CURRENCY_CONVERSION_PREFIX: Final[str] = ""

CURRENCY_CONVERSION_TAG: Final[str] = "Currency Conversion"


def create_api() -> FastAPI:
    api = FastAPI(root_path=API_PREFIX)
    api.include_router(
        router=convert_currency_endpoint.router,
        prefix=CURRENCY_CONVERSION_PREFIX,
        tags=[CURRENCY_CONVERSION_TAG],
    )

    return api
