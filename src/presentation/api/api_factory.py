from contextlib import asynccontextmanager
from typing import Final

from fastapi import FastAPI

from dependency_injection import init_postgre_sql_database
from .routes.currency_conversion import convert_currency_endpoint
from .routes.auth import login_endpoint


API_PREFIX: Final[str] = "/api/v1"
AUTH_PREFIX: Final[str] = ""
CURRENCY_CONVERSION_PREFIX: Final[str] = ""

AUTH_TAG: Final[str] = "Auth"
CURRENCY_CONVERSION_TAG: Final[str] = "Currency Conversion"


@asynccontextmanager
async def lifespan(api: FastAPI):
    init_postgre_sql_database()
    yield


def create_api() -> FastAPI:
    api = FastAPI(root_path=API_PREFIX, lifespan=lifespan)

    api.include_router(
        router=login_endpoint.router,
        prefix=AUTH_PREFIX,
        tags=[AUTH_TAG],
    )

    api.include_router(
        router=convert_currency_endpoint.router,
        prefix=CURRENCY_CONVERSION_PREFIX,
        tags=[CURRENCY_CONVERSION_TAG],
    )

    return api
