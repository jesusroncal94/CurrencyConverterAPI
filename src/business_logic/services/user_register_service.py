from dataclasses import dataclass
from ..domain import User, UserCreation
from ..repositories import UserRepository


@dataclass(frozen=True)
class UserRegisterServiceParams:
    user_creation: UserCreation


@dataclass(frozen=True)
class UserRegisterServiceResponse:
    user: User


class UserRegisterService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def run(
        self, params: UserRegisterServiceParams
    ) -> UserRegisterServiceResponse:
        user = await self.user_repository.create_user(
            user_creation=params.user_creation
        )

        return user
