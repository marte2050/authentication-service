from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import table_registry


@table_registry.mapped_as_dataclass
class Group:
    """Represents a group in the system with associated details.

    Attributes:
        id (int): Primary key, unique identifier for the group.
        name (str): Unique name for the group.
        description (str): Description of the group.
        created_at (str): Timestamp of when the group was created.
        updated_at (str): Timestamp of the last update to the group record.

    Example:
        >>> new_group = Group(
        ...     name="admin",
        ...     description="Administrators group"
        ... )
        >>> session.add(new_group)
        >>> session.commit()
    """

    __tablename__ = "group"
    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[str] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[str] = mapped_column(init=False, server_default=func.now(), onupdate=func.now())

    users = relationship("User", secondary="user_groups", back_populates="groups")
    permissions = relationship("Permission", secondary="group_permissions", back_populates="groups")
