from typing import Annotated
from typing import Final

from business_logic import UserRegisterService, UserRegisterServiceParams, UserCreation
from dependency_injection import get_user_register_service
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from pydantic import BaseModel
from pydantic import Field


ENDPOINT_NAME: Final[str] = "Register"
ERROR_MSG: Final[str] = (
    "fatal error in endpoint {endpoint_name}: {exception_description}"
)

CODE_FIELD: Final[str] = "code"
MESSAGE_FIELD: Final[str] = "message"

USER_NAME_FIELD: Final[str] = "username"
PASSWORD_FIELD: Final[str] = "password"

USER_FIELD: Final[str] = "user"

router = APIRouter()


class UserDTO(BaseModel):
    id: 
    user_name: str = Field(alias=USER_NAME_FIELD)


class RegisterRequestBody(BaseModel):
    user_name: str = Field(alias=USER_NAME_FIELD)
    password: str = Field(alias=PASSWORD_FIELD)


class RegisterResponseBody(BaseModel):
    user: UserDTO = Field(alias=USER_FIELD)


@router.post(
    path="/registeruser",
    response_model=RegisterResponseBody,
    name=ENDPOINT_NAME,
)
async def convert_currency(
    request_body: RegisterRequestBody,
    user_register_service: Annotated[
        UserRegisterService, Depends(dependency=get_user_register_service)
    ],
    response: Response = Response(),
):
    try:
        user_register_service_response = await user_register_service.run(
            params=UserRegisterServiceParams(
                user_creation=UserCreation(
                    user_name=request_body.user_name, password=request_body.password
                )
            )
        )

        return RegisterResponseBody.model_construct(user=UserDTO.model_construct(user=UserDTO.model_construct(user_name=user_register_service_response.user.user_name)))
    except Exception as exception:
        error_msg = ERROR_MSG.format(
            endpoint_name=ENDPOINT_NAME,
            exception_description=exception,
        )
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return {CODE_FIELD: response.status_code, MESSAGE_FIELD: error_msg}
