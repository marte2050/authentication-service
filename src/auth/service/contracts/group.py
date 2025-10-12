from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from auth.model import Group
from auth.repository.contracts import IGroupRepository, IPermissionRepository


class IGroupService(ABC):
    """Interface for Group Service.

    Methods:
        - get_group_by_id(group_id: int)
        - get_group_by_name(name: str)
        - create_group(group_data: dict)
        - update_group(group_id: int, group_data: dict)
        - delete_group(group_id: int)
        - add_permission_to_group(group_id: int, permission_id: int)
        - add_user_to_group(group_id: int, user_id: int)
    """

    @abstractmethod
    def __init__(
        self,
        session: Session,
        group_repository: IGroupRepository,
        permission_repository: IPermissionRepository,
    ) -> None:
        """Initialize the GroupService with required repositories and session.

        Args:
            session (Session): The database session.
            group_repository (IGroupRepository): The group repository interface.
            permission_repository (IPermissionRepository): The permission repository interface.

        Returns:
            None
        """

    @abstractmethod
    def get_group_by_id(self, group_id: int) -> Group | None:
        """Get a group by its ID.

        Args:
            group_id (int): The ID of the group to retrieve.

        Returns:
            Group: The group object if found.

        Raises:
            HTTPException: If the group is not found (status code 404).
        """

    @abstractmethod
    def get_group_by_name(self, name: str) -> Group | None:
        """Get a group by its name.

        Args:
            name (str): The name of the group to retrieve.

        Returns:
            Group: The group object if found.
            None: If the group is not found.
        """

    @abstractmethod
    def create_group(self, group_data: dict) -> Group:
        """Create a new group.

        Args:
            group_data (dict): The data for the new group.

        Returns:
            Group: The created group object.

        Raises:
            HTTPException: If the group already exists (status code 400).
        """

    @abstractmethod
    def update_group(self, group_id: int, group_data: dict) -> Group:
        """Update a group by its ID.

        Args:
            group_id (int): The ID of the group to update.
            group_data (dict): The data to update the group with.

        Returns:
            Group: The updated group object.

        Raises:
            HTTPException: If the group is not found (status code 404).
        """

    @abstractmethod
    def delete_group(self, group_id: int) -> dict:
        """Delete a group by its ID.

        Args:
            group_id (int): The ID of the group to delete.

        Returns:
            dict: A message indicating successful deletion.

        Raises:
            HTTPException: If the group is not found (status code 404).
        """

    @abstractmethod
    def add_permission_to_group(self, group_id: int, permission_id: int) -> dict:
        """Add a permission to a group.

        Args:
            group_id (int): The ID of the group.
            permission_id (int): The ID of the permission to add.

        Returns:
            dict: A message indicating successful addition.

        Raises:
            HTTPException: If the group or permission is not found (status code 404).
            HTTPException: If the permission is already assigned to the group (status code 400).
        """

    @abstractmethod
    def add_user_to_group(self, group_id: int, user_id: int) -> dict:
        """Add a user to a group.

        Args:
            group_id (int): The ID of the group.
            user_id (int): The ID of the user to add.

        Returns:
            dict: A message indicating successful addition.

        Raises:
            HTTPException: If the group or user is not found (status code 404).
            HTTPException: If the user is already assigned to the group (status code 400).
        """
