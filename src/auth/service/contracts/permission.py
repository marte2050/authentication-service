from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from auth.model import Permission
from auth.repository.contracts import IGroupRepository, IPermissionRepository


class IPermissionService(ABC):
    """Interface for Permission Service.

    Methods:
        - get_permission_by_id(permission_id: int) -> Permission
        - get_permission_by_name(name: str)
        - create_permission(permission_data: dict) -> Permission
        - update_permission(permission_id: int, permission_data: dict)
        - delete_permission(permission_id: int)
    """

    @abstractmethod
    def __init__(
        self,
        session: Session,
        permission_repository: IPermissionRepository,
        group_repository: IGroupRepository,
    ) -> None:
        """Initialize the PermissionService with required repositories and session.

        Args:
            session (Session): The database session.
            permission_repository (IPermissionRepository): The permission repository interface.
            group_repository (IGroupRepository): The group repository interface.

        Returns:
            None
        """

    @abstractmethod
    def get_permission_by_id(self, permission_id: int) -> Permission:
        """Get a permission by its ID.

        Args:
            permission_id (int): The ID of the permission to retrieve.

        Returns:
            Permission: The permission object if found.

        Raises:
            HTTPException: If the permission is not found (status code 404).
        """

    @abstractmethod
    def get_permission_by_name(self, name: str) -> Permission | None:
        """Get a permission by its name.

        Args:
            name (str): The name of the permission to retrieve.

        Returns:
            Permission: The permission object if found.

        Raises:
            HTTPException: If the permission is not found (status code 404).
        """

    @abstractmethod
    def create_permission(self, permission_data: dict) -> Permission:
        """Create a new permission.

        Args:
            permission_data (dict): A dictionary containing the permission data.

        Returns:
            Permission: The created permission object.

        Raises:
            HTTPException: If a permission with the same name already exists (status code 400).
        """

    @abstractmethod
    def update_permission(self, permission_id: int, permission_data: dict) -> Permission:
        """Update an existing permission.

        Args:
            permission_id (int): The ID of the permission to update.
            permission_data (dict): A dictionary containing the updated permission data.

        Raises:
            HTTPException: If the permission is not found (status code 404).

        Returns:
            Permission: The updated permission object if found, else False.
        """

    @abstractmethod
    def delete_permission(self, permission_id: int) -> dict:
        """Delete a permission by its ID.

        Args:
            permission_id (int): The ID of the permission to delete.

        Raises:
            HTTPException: If the permission is not found (status code 404).

        Returns:
            dict: A message indicating successful deletion.
        """
