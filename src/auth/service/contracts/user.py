from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from auth.model import User
from auth.repository.contracts import IUserRepository, IGroupRepository
from utils.security.contracts import ICriptografy


class IUserService(ABC):
    @abstractmethod
    def __init__(
        self, 
        session: Session, 
        user_repository: IUserRepository, 
        group_repository: IGroupRepository, 
        criptografy: ICriptografy
    ) -> None:
        ...

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> None | User:
        ...

    @abstractmethod
    def get_user_by_username(self, username: str) -> None | User:
        ...

    @abstractmethod
    def get_user_by_email(self, email: str) -> None | User:
        ...

    @abstractmethod
    def create_user(self, user_data: dict)-> None | User:
        ...

    @abstractmethod
    def update_user(self, user_id: int, user_data: dict) -> None | User:
        ...

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        ...

    @abstractmethod
    def change_password(self, user_id: int, new_password: str) -> bool:
        ...

    @abstractmethod
    def add_group_to_user(self, user_id: int, group_id: int) -> bool:
        ...

    @abstractmethod
    def authenticate(self, username: str, password: str) -> None | User:
        ...