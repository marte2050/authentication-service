from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from auth.repository.contracts import IGroupRepository, IPermissionRepository


class IGroupService(ABC):
    @abstractmethod
    def __init__(
        self,
        session: Session,
        group_repository: IGroupRepository,
        permission_repository: IPermissionRepository,
    ) -> None: ...

    @abstractmethod
    def get_group_by_id(self, group_id: int): ...

    @abstractmethod
    def get_group_by_name(self, name: str): ...

    @abstractmethod
    def create_group(self, group_data: dict): ...

    @abstractmethod
    def update_group(self, group_id: int, group_data: dict): ...

    @abstractmethod
    def delete_group(self, group_id: int): ...

    @abstractmethod
    def add_permission_to_group(self, group_id: int, permission_id: int): ...

    @abstractmethod
    def add_user_to_group(self, group_id: int, user_id: int): ...
