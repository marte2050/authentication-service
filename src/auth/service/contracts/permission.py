from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from auth.repository.contracts import IGroupRepository, IPermissionRepository


class IPermissionService(ABC):
    @abstractmethod
    def __init__(
        self,
        session: Session,
        permission_repository: IPermissionRepository,
        group_repository: IGroupRepository,
    ) -> None: ...

    @abstractmethod
    def get_permission_by_id(self, permission_id: int): ...

    @abstractmethod
    def get_permission_by_name(self, name: str): ...

    @abstractmethod
    def create_permission(self, permission_data: dict): ...

    @abstractmethod
    def update_permission(self, permission_id: int, permission_data: dict): ...

    @abstractmethod
    def delete_permission(self, permission_id: int): ...
