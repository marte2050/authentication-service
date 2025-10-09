from sqlalchemy.orm import Session
from auth.model import Group
from auth.repository.contracts import IGroupRepository


class GroupService():
    def __init__(
        self, 
        session: Session, 
        group_repository: IGroupRepository
    ) -> None:
        self.group_repository: IGroupRepository = group_repository(session)

    def get_group_by_id(self, group_id: int) -> Group | None:
        return self.group_repository.get_by_id(group_id)

    def get_group_by_name(self, name: str):
        return self.group_repository.get_by_name(name)

    def create_group(self, group_data: dict):
        group_existed = self.group_repository.get_by_name(group_data["name"])

        if group_existed:
            return None
        
        group = Group(**group_data)
        return self.group_repository.create(group)

    def update_group(self, group_id: int, group_data: dict):
        group_existed = self.group_repository.get_by_id(group_id)

        if not group_existed:
            return None

        group_existed.name = group_data["name"]
        group_existed.description = group_data["description"]
        return self.group_repository.update(group_existed)

    def delete_group(self, group_id: int):
        group_existed = self.group_repository.get_by_id(group_id)

        if not group_existed:
            return False

        self.group_repository.delete(group_existed)
        return True

    def add_permission_to_group(self, group_id: int, permission_id: int):
        ...

    def add_user_to_group(self, group_id: int, user_id: int):
        ...