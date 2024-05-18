from typing import Annotated
from typing import Final

from business_logic import Currency
from business_logic import CurrencyConverterService
from dependency_injection import get_currency_converter_service
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from fastapi import Response
from fastapi import status
from pydantic import BaseModel
from pydantic import Field


ENDPOINT_NAME: Final[str] = "Convert Currency"
ERROR_MSG: Final[str] = (
    "fatal error in endpoint {endpoint_name}: {exception_description}"
)

CODE_FIELD: Final[str] = "code"
MESSAGE_FIELD: Final[str] = "message"

AMOUNT_QUERY_PARAM: Final[str] = "amount"
FROM_CURRENCY_QUERY_PARAM: Final[str] = "fromcurrency"
TO_CURRENCY_QUERY_PARAM: Final[str] = "tocurrency"

RESULT_FIELD: Final[str] = "result"

router = APIRouter()


class ConvertCurrencyResponseBody(BaseModel):
    result: float = Field(alias=RESULT_FIELD)


@router.get(
    path="/convertcurrency",
    response_model=ConvertCurrencyResponseBody,
    name=ENDPOINT_NAME,
)
async def convert_currency(
    currency_converter_service: Annotated[
        CurrencyConverterService, Depends(dependency=get_currency_converter_service)
    ],
    amount: float = Query(alias=AMOUNT_QUERY_PARAM),
    from_currency: Currency = Query(alias=FROM_CURRENCY_QUERY_PARAM),
    to_currency: Currency = Query(alias=TO_CURRENCY_QUERY_PARAM),
    response: Response = Response(),
):
    try:
        result = await currency_converter_service.convert_currency(
            amount=amount, from_currency=from_currency, to_currency=to_currency
        )

        return ConvertCurrencyResponseBody.model_construct(result=result)
    except Exception as exception:
        error_msg = ERROR_MSG.format(
            endpoint_name=ENDPOINT_NAME,
            exception_description=exception,
        )
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return {CODE_FIELD: response.status_code, MESSAGE_FIELD: error_msg}
