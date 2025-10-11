from sqlalchemy import select
from sqlalchemy.orm import Session

from auth.model import Group, User
from auth.repository.contracts import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> User:
        return self.session.get(User, user_id)

    def get_by_username(self, username: str) -> User:
        stmt = select(User).where(User.username == username)
        return self.session.execute(stmt).scalar_one_or_none()

    def get_by_email(self, email: str) -> User:
        stmt = select(User).where(User.email == email)
        return self.session.execute(stmt).scalar_one_or_none()

    def create(self, user: dict) -> User:
        user = User(**user)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update(self, user: User) -> User:
        self.session.merge(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()

    def add_group(self, user: User, group_id: int) -> None:
        if group_id not in [group.id for group in user.groups]:
            stmt = select(Group).where(Group.id == group_id)
            group = self.session.execute(stmt).scalar_one_or_none()
            if group:
                user.groups.append(group)
                self.session.commit()

    def get_all_groups(self, user: User) -> list | None:
        return user.groups

    def get_all_permissions(self, groups: list[Group]) -> list | None:
        permissions = []

        if not groups:
            return permissions

        for group in groups:
            permissions_group = group.permissions

            for permission in permissions_group:
                permissions.append(permission.name)

        return permissions
