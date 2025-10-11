from sqlalchemy import select
from sqlalchemy.orm import Session

from auth.model import Group, Permission, User
from auth.repository.contracts import IGroupRepository


class GroupRepository(IGroupRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, group_id: int) -> Group:
        return self.session.get(Group, group_id)

    def get_by_name(self, name: str) -> Group:
        stmt = select(Group).where(Group.name == name)
        return self.session.execute(stmt).scalar_one_or_none()

    def create(self, group: Group) -> Group:
        self.session.add(group)
        self.session.commit()
        self.session.refresh(group)
        return group

    def update(self, group: Group) -> Group:
        self.session.merge(group)
        self.session.commit()
        self.session.refresh(group)
        return group

    def delete(self, group: Group) -> None:
        self.session.delete(group)
        self.session.commit()

    def add_user(self, group: Group, user_id: int) -> None:
        if user_id not in [user.id for user in group.users]:
            stmt = select(User).where(User.id == user_id)
            user = self.session.execute(stmt).scalar_one_or_none()
            if user:
                group.users.append(user)
                self.session.commit()

    def add_permission(self, group: Group, permission_id: int) -> None:
        stmt = select(Permission).where(Permission.id == permission_id)
        permission = self.session.execute(stmt).scalar_one_or_none()
        group.permissions.append(permission)
        self.session.commit()
