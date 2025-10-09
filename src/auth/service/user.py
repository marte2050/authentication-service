from sqlalchemy.orm import Session
from auth.model import User
from auth.service.contracts import IUserService as IUserService
from auth.repository.contracts import IUserRepository, IGroupRepository
from utils.security.contracts import ICriptografy


class UserService(IUserService):
    def __init__(
        self, 
        session: Session, 
        user_repository: IUserRepository, 
        group_repository: IGroupRepository, 
        criptografy: ICriptografy
    ) -> None:
        self.user_repository: IUserRepository = user_repository(session)
        self.group_repository: IGroupRepository = group_repository(session)
        self.criptografy: ICriptografy = criptografy()
        
    def get_user_by_id(self, user_id: int) -> None | User:
        return self.user_repository.get_by_id(user_id)

    def get_user_by_username(self, username: str) -> None | User:
        return self.user_repository.get_by_username(username)

    def get_user_by_email(self, email: str) -> None | User:
        return self.user_repository.get_by_email(email)

    def create_user(self, user_data: dict) -> None | User:
        username_exists = self.user_repository.get_by_username(user_data["username"])
        email_exists = self.user_repository.get_by_email(user_data["email"])
    
        if username_exists or email_exists:
            return None
        
        password_hashed = self.criptografy.hash_password(user_data["password"])

        data = {
            "username": user_data["username"],
            "email": user_data["email"],
            "hashed_password": password_hashed
        }

        user = User(**data)
        return self.user_repository.create(user)

    def update_user(self, user_id: int, user_data: dict) -> None | User:
        user_existed = self.user_repository.get_by_id(user_id)
        username_already_used = self.user_repository.get_by_username(user_data["username"])
        email_already_used = self.user_repository.get_by_email(user_data["email"])

        if not user_existed or email_already_used or username_already_used:
            return None     

        user_existed.email = user_data["email"]
        user_existed.username = user_data["username"]
        return self.user_repository.update(user_existed)

    def delete_user(self, user_id: int) -> bool:
        user_existed = self.user_repository.get_by_id(user_id)

        if not user_existed:
            return False

        self.user_repository.delete(user_existed)
        return True

    def change_password(self, user_id: int, new_password: str) -> bool:
        user_existed = self.user_repository.get_by_id(user_id)

        if not user_existed:
            return False

        password_hashed = self.criptografy.hash_password(new_password)
        user_existed.hashed_password = password_hashed
        self.user_repository.update(user_existed)
        return True

    def add_group_to_user(self, user_id: int, group_id: int) -> bool:
        user_existed = self.user_repository.get_by_id(user_id)
        group_existed = self.group_repository.get_by_id(group_id)

        if not user_existed or not group_existed:
            return False
        
        self.user_repository.add_group(user_existed, group_id)
        return True