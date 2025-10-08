from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func
from database import table_registry


@table_registry.mapped_as_dataclass
class Permission:
    """
    Permission model for the application.
    Represents a permission in the system with associated details.

    Attributes:
        id (int): Primary key, unique identifier for the permission.
        name (str): Unique name for the permission.
        description (str): Description of the permission.
        created_at (str): Timestamp of when the permission was created.
        updated_at (str): Timestamp of the last update to the permission record.

    Example:
        >>> new_permission = Permission(
        ...     name="read",
        ...     description="Read permission"
        ... )
        >>> session.add(new_permission)
        >>> session.commit()
    """

    __tablename__ = "permission"
    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[str] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[str] = mapped_column(init=False, server_default=func.now(), onupdate=func.now())

    groups = relationship("Group", secondary="group_permissions", back_populates="permissions")