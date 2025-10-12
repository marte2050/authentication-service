from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from auth.model import Group, User
from auth.repository.contracts import IGroupRepository, IUserRepository
from utils.security.contracts import ICriptografy


class IUserService(ABC):
    """Interface for User Service.

    Methods:
        - get_user_by_id
        - get_user_by_username
        - get_user_by_email
        - create_user
        - update_user
        - delete_user
        - change_password
        - add_group_to_user
        - authenticate
        - get_groups
        - get_permissions
        - verify_permission
    """

    @abstractmethod
    def __init__(
        self,
        session: Session,
        user_repository: IUserRepository,
        group_repository: IGroupRepository,
        criptografy: ICriptografy,
    ) -> None:
        """Initialize User Service.

        Args:
            session (Session): SQLAlchemy session
            user_repository (IUserRepository): User repository
            group_repository (IGroupRepository): Group repository
            criptografy (ICriptografy): Criptografy service
        """

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        """Get user by ID.

        Args:
            user_id (int): User ID

        Raises:
            HTTPException: If user not found

        Returns:
            User: User object or None if not found
        """

    @abstractmethod
    def get_user_by_username(self, username: str) -> None | User:
        """Get user by username.

        Args:
            username (str): Username

        Raises:
            HTTPException: If user not found

        Returns:
            User: User object or None if not found
        """

    @abstractmethod
    def get_user_by_email(self, email: str) -> None | User:
        """Get user by email.

        Args:
            email (str): User email

        Raises:
            HTTPException: If user not found

        Returns:
            User: User object or None if not found
        """

    @abstractmethod
    def create_user(self, user_data: dict) -> User:
        """Create a new user.

        Args:
            user_data (dict): User data

        Raises:
            HTTPException: If username or email already in use

        Returns:
            User: Created user object
        """

    @abstractmethod
    def update_user(self, user_id: int, user_data: dict) -> User:
        """Update user information.

        Args:
            user_id (int): User ID
            user_data (dict): Updated user data

        Raises:
            HTTPException: If user not found

        Returns:
            User: Updated user object
        """

    @abstractmethod
    def delete_user(self, user_id: int) -> dict:
        """Delete a user.

        Args:
            user_id (int): User ID

        Raises:
            HTTPException: If user not found

        Returns:
            dict: Deletion status message
        """

    @abstractmethod
    def change_password(self, user_id: int, new_password: str) -> str:
        """Change user password.

        Args:
            user_id (int): User ID
            new_password (str): New password

        Raises:
            HTTPException: If user not found

        Returns:
            str: Password change status message
        """

    @abstractmethod
    def add_group_to_user(self, user_id: int, group_id: int) -> bool:
        """Add a group to a user.

        Args:
            user_id (int): User ID
            group_id (int): Group ID

        Raises:
            HTTPException: If user or group not found

        Returns:
            bool: True if group added successfully
        """

    @abstractmethod
    def authenticate(self, username: str, password: str) -> dict:
        """Authenticate a user.

        Args:
            username (str): Username
            password (str): Password

        Raises:
            HTTPException: If authentication fails

        Returns:
            User: Authenticated user object or None if authentication fails
        """

    @abstractmethod
    def get_groups(self, user: User) -> list:
        """Get groups of a user.

        Args:
            user (User): User object

        Returns:
            list: List of groups
        """

    @abstractmethod
    def get_permissions(self, group: Group) -> list:
        """Get permissions of a group.

        Args:
            group (Group): Group object

        Returns:
            list: List of permissions
        """

    @abstractmethod
    def verify_permission(self, email: str, permission_name: str) -> User:
        """Verify if a user has a specific permission.

        Args:
            email (str): User email
            permission_name (str): Permission name

        Raises:
            HTTPException: If user not found or has no groups

        Returns:
            User: User object if permission is verified
        """
