from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from auth.model import User


class IUserRepository(ABC):
    """
    Interface for User repository

    Methods:
        - init - initialize with a database session
        - get_by_id
        - get_by_username
        - get_by_email
        - create
        - update
        - delete
        - add_group
    """

    @abstractmethod
    def __init__(self, session: Session):
        ...

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        ...

    @abstractmethod
    def get_by_username(self, username: str) -> User:
        ...

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        ...

    @abstractmethod
    def create(self, user: User) -> User:
        ...

    @abstractmethod
    def update(self, user: User) -> User:
        ...

    @abstractmethod
    def delete(self, user: User) -> None:
        ...

    @abstractmethod
    def add_group(self, user: User, group_id: int) -> None:
        ...