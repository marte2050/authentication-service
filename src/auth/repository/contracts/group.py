from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from auth.model import Group


class IGroupRepository(ABC):
    """Interface for group repository.

    Methods:
        - init - initialize with a database session
        - get_by_id
        - get_by_name
        - create
        - update
        - delete
        - add_user
    """

    @abstractmethod
    def __init__(self, session: Session): ...

    @abstractmethod
    def get_by_id(self, group_id: int) -> Group: ...

    @abstractmethod
    def get_by_name(self, name: str) -> Group: ...

    @abstractmethod
    def create(self, group: Group) -> Group: ...

    @abstractmethod
    def update(self, group: Group) -> Group: ...

    @abstractmethod
    def delete(self, group: Group) -> None: ...

    @abstractmethod
    def add_user(self, group: Group, user_id: int) -> None: ...

    @abstractmethod
    def add_permission(self, group: Group, permission_id: int) -> None: ...
