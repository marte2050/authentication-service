from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from auth.model import Permission
from auth.repository.contracts import IGroupRepository, IPermissionRepository
from auth.service.contracts.permission import IPermissionService


class PermissionService(IPermissionService):
    def __init__(
        self,
        session: Session,
        permission_repository: IPermissionRepository,
        group_repository: IGroupRepository,
    ) -> None:
        self.session = session
        self.permission_repository: IPermissionRepository = permission_repository(session)
        self.group_repository: IGroupRepository = group_repository(session)

    def get_permission_by_id(self, permission_id: int):
        permission_existed = self.permission_repository.get_by_id(permission_id)

        if not permission_existed:
            raise HTTPException(status_code=404, detail="Permission not found.")

        return permission_existed

    def get_permission_by_name(self, name: str):
        return self.permission_repository.get_by_name(name)

    def create_permission(self, permission_data: dict):
        permission_existed = self.get_permission_by_name(permission_data["name"])

        if permission_existed:
            raise HTTPException(status_code=400, detail="Permission with this name already exists.")

        permission = Permission(**permission_data)
        return self.permission_repository.create(permission)

    def update_permission(self, permission_id: int, permission_data: dict):
        permission_existed = self.get_permission_by_id(permission_id)

        if not permission_existed:
            return False

        permission_existed.name = permission_data.get("name", permission_existed.name)
        permission_existed.description = permission_data.get("description", permission_existed.description)
        permission = self.permission_repository.update(permission_existed)
        return permission

    def delete_permission(self, permission_id: int):
        permission_existed = self.get_permission_by_id(permission_id)

        if not permission_existed:
            raise HTTPException(status_code=404, detail="Permission not found.")

        self.permission_repository.delete(permission_existed)
        return {"detail": "Permission deleted successfully."}
