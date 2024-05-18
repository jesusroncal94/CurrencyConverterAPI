from business_logic import User, UserRepository, UserCreation
from ..data_sources import PostgreSQLDataSource
from ..entities import UserCreationModel, UserModel


class UserRepositoryImplemented(UserRepository):
    def __init__(self, postgre_sql_data_source: PostgreSQLDataSource) -> None:
        self.postgre_sql_data_source = postgre_sql_data_source

    def create_user(self, user_creation: UserCreation) -> User:
        user_creation_model = self._map_user_creation_to_user_creation_model(
            user_creation=user_creation
        )
        self.postgre_sql_data_source.create_user(
            user_creation_model=user_creation_model
        )

    @classmethod
    def _map_user_creation_to_user_creation_model(
        cls, user_creation: UserCreation
    ) -> UserCreationModel:
        return UserCreationModel.model_construct(
            user_name=user_creation.user_name,
            password=user_creation.password,
        )

    @classmethod
    def _map_user_model_to_user(cls, user_model: UserModel) -> User:
        return User(
            id=user_model.id,
            user_name=user_model.user_name,
            hashed_password=user_model.hashed_password,
        )
