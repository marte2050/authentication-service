from abc import ABC, abstractmethod

class IUserService(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int):
        ...

    @abstractmethod
    def get_user_by_username(self, username: str):
        ...

    @abstractmethod
    def get_user_by_email(self, email: str):
        ...

    @abstractmethod
    def create_user(self, user_data: dict):
        ...

    @abstractmethod
    def update_user(self, user_id: int, user_data: dict):
        ...

    @abstractmethod
    def delete_user(self, user_id: int):
        ...

    @abstractmethod
    def change_password(self, user_id: int, new_password: str):
        ...

    @abstractmethod
    def add_group_to_user(self, user_id: int, group_id: int):
        ...