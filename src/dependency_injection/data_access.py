from typing import Annotated

from business_logic import CurrencyConverterRepository
from business_logic import UserRepository
from data_access import CurrencyConverterRepositoryImplemented
from data_access import ExchangeRatesDataAPI
from data_access import UserRepositoryImplemented
from data_access import PostgreSQLDataSource
from fastapi import Depends
from sqlmodel import Session, create_engine, SQLModel

from .settings import get_settings
from .settings import Settings


def get_postgre_sql_engine(
    settings: Annotated[Settings, Depends(dependency=get_settings)],
):
    return create_engine(url=settings.postgre_sql_url, echo=True)


def init_postgre_sql_database(
    postgre_sql_engine=get_postgre_sql_engine(settings=get_settings()),
) -> None:
    SQLModel.metadata.create_all(postgre_sql_engine)


def get_postgre_sql_session(
    postgre_sql_engine=Depends(dependency=get_postgre_sql_engine),
) -> Session:
    return Session(postgre_sql_engine)


def get_exchange_rates_data_api(
    settings: Annotated[Settings, Depends(dependency=get_settings)],
) -> ExchangeRatesDataAPI:
    return ExchangeRatesDataAPI(
        api_key=settings.exchange_rates_data_api_key,
        currency_conversion_endpoint=settings.exchange_rates_data_api_currency_conversion_endpoint,
    )


def get_postgre_sql_data_source(
    postgre_sql_session: Annotated[
        Session, Depends(dependency=get_postgre_sql_session)
    ],
) -> PostgreSQLDataSource:
    return PostgreSQLDataSource(session=postgre_sql_session)


def get_currency_converter_repository(
    exchange_rates_data_api: Annotated[
        ExchangeRatesDataAPI, Depends(dependency=get_exchange_rates_data_api)
    ],
) -> CurrencyConverterRepository:
    return CurrencyConverterRepositoryImplemented(
        exchange_rates_data_api=exchange_rates_data_api
    )


def get_user_repository(
    postgre_sql_data_source: Annotated[
        PostgreSQLDataSource, Depends(dependency=get_exchange_rates_data_api)
    ],
) -> UserRepository:
    return UserRepositoryImplemented(postgre_sql_data_source=postgre_sql_data_source)
