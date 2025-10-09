from sqlalchemy import select
from sqlalchemy.orm import Session
from auth.model import Permission, Group
from auth.repository.contracts import IPermissionRepository


class PermissionRepository(IPermissionRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int) -> Permission:
        return self.session.get(Permission, id)

    def get_by_name(self, name: str) -> Permission:
        stmt = select(Permission).where(Permission.name == name)
        return self.session.execute(stmt).scalar_one_or_none()

    def create(self, permission: Permission) -> Permission:
        self.session.add(permission)
        self.session.commit()
        self.session.refresh(permission)
        return permission

    def update(self, permission: Permission) -> Permission:
        self.session.merge(permission)
        self.session.commit()
        self.session.refresh(permission)
        return permission

    def delete(self, permission: Permission) -> None:
        self.session.delete(permission)
        self.session.commit()

    def add_to_group(self, permission: Permission, group_id: int) -> None:
        if group_id not in [group.id for group in permission.groups]:
            stmt = select(Group).where(Group.id == group_id)
            group = self.session.execute(stmt).scalar_one_or_none()
            if group:
                permission.groups.append(group)
                self.session.commit()