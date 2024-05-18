from typing import Final

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from pydantic import BaseModel
from pydantic import Field


ENDPOINT_NAME: Final[str] = "Login"
ERROR_MSG: Final[str] = (
    "fatal error in endpoint {endpoint_name}: {exception_description}"
)

CODE_FIELD: Final[str] = "code"
MESSAGE_FIELD: Final[str] = "message"

USER_NAME_FIELD: Final[str] = "username"
PASSWORD_FIELD: Final[str] = "password"

TOKEN_FIELD: Final[str] = "token"

router = APIRouter()


class LoginRequestBody(BaseModel):
    user_name: str = Field(alias=USER_NAME_FIELD)
    password: str = Field(alias=PASSWORD_FIELD)


class LoginResponseBody(BaseModel):
    token: str = Field(alias=TOKEN_FIELD)


@router.post(
    path="/login",
    response_model=LoginResponseBody,
    name=ENDPOINT_NAME,
)
async def login(
    request_body: LoginRequestBody,
    # user_register_service: Annotated[
    #     UserRegisterService, Depends(dependency=get_user_register_service)
    # ],
    response: Response = Response(),
):
    try:
        return LoginResponseBody.model_construct(token="asasasas")
    except Exception as exception:
        error_msg = ERROR_MSG.format(
            endpoint_name=ENDPOINT_NAME,
            exception_description=exception,
        )
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return {CODE_FIELD: response.status_code, MESSAGE_FIELD: error_msg}
