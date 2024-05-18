from abc import ABC
from abc import abstractmethod

from ..domain import User, UserCreation


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user_creation: UserCreation) -> User:
        pass
