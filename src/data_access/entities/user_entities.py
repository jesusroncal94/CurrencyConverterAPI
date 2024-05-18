from passlib.context import CryptContext
from pydantic import model_validator
from sqlmodel import SQLModel, Field
from typing import Final, Optional
from typing_extensions import Self
from uuid import UUID, uuid4


ID_FIELD: Final[str] = "id"
USER_NAME_FIELD: Final[str] = "username"
HASHED_PASSWORD_FIELD: Final[str] = "hashedpassword"

CRYPT_CONTEXT: Final[CryptContext] = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserModel(SQLModel, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        alias=ID_FIELD,
        primary_key=True,
        nullable=False,
        index=True,
    )
    user_name: str = Field(alias=USER_NAME_FIELD)
    hashed_password: Optional[str] = Field(default=None, alias=HASHED_PASSWORD_FIELD)


class UserCreationModel(UserModel):
    password: str

    @model_validator(mode="before")
    def set_hashed_password(self) -> Self:
        self.hashed_password = CRYPT_CONTEXT.hash(self.password)

        return self
