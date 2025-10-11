from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from auth.model import Permission


class IPermissionRepository(ABC):
    """Interface for permission repository.

    Methods:
        - init - initialize with a database session
        - get_by_id
        - get_by_name
        - create
        - update
        - delete
        - add_to_group
    """

    @abstractmethod
    def __init__(self, session: Session): ...

    @abstractmethod
    def get_by_id(self, id: int) -> Permission: ...

    @abstractmethod
    def get_by_name(self, name: str) -> Permission: ...

    @abstractmethod
    def create(self, permission: Permission) -> Permission: ...

    @abstractmethod
    def update(self, permission: Permission) -> Permission: ...

    @abstractmethod
    def delete(self, permission: Permission) -> None: ...

    @abstractmethod
    def add_to_group(self, permission: Permission, group_id: int) -> None: ...
