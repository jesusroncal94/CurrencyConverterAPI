from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass(frozen=True)
class User:
    id: UUID
    user_name: str
    hashed_password: Optional[str] = None


@dataclass(frozen=True)
class UserCreation:
    user_name: str
    password: str
