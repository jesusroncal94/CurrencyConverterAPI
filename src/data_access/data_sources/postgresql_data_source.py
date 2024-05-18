from sqlmodel import Session, select
from typing import Optional

from ..entities import UserModel, UserCreationModel


class PostgreSQLDataSource:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_user(self, user_creation_model: UserCreationModel) -> UserModel:
        with self.session:
            self.session.add(user_creation_model)
            self.session.commit()
            self.session.refresh(user_creation_model)
            user_model = self._map_from_user_creation_model_to_user_model(
                user_creation_model=user_creation_model
            )

            return user_model

    def get_user_by_user_name(self, user_name: str) -> Optional[UserModel]:
        with self.session:
            statement = select(UserModel).where(UserModel.user_name == user_name)
            user = self.session.exec(statement=statement).first()

            return user

    @classmethod
    def _map_from_user_creation_model_to_user_model(
        cls, user_creation_model: UserCreationModel
    ) -> UserModel:
        return UserModel.model_construct(
            id=user_creation_model.id,
            user_name=user_creation_model.user_name,
            hashed_password=user_creation_model.hashed_password,
        )
