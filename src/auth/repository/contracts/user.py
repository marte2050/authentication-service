from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from auth.model import Group, User


class IUserRepository(ABC):
    """Interface for User repository.

    Methods:
        - init - initialize with a database session
        - get_by_id
        - get_by_username
        - get_by_email
        - create
        - update
        - delete
        - add_group
        - get_all_groups
        - get_all_permissions
    """

    @abstractmethod
    def __init__(self, session: Session): ...

    @abstractmethod
    def get_by_id(self, user_id: int) -> User: ...

    @abstractmethod
    def get_by_username(self, username: str) -> User: ...

    @abstractmethod
    def get_by_email(self, email: str) -> User: ...

    @abstractmethod
    def create(self, user: dict) -> User: ...

    @abstractmethod
    def update(self, user: User) -> User: ...

    @abstractmethod
    def delete(self, user: User) -> None: ...

    @abstractmethod
    def add_group(self, user: User, group_id: int) -> None: ...

    @abstractmethod
    def get_all_groups(self, user: User) -> list | None: ...

    @abstractmethod
    def get_all_permissions(self, groups: Group) -> list | None: ...
