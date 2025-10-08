from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func
from database import table_registry


@table_registry.mapped_as_dataclass
class User:
    """
    User model for the application.
    Represents a user in the system with authentication details.

    Attributes:
        id (int): Primary key, unique identifier for the user.
        username (str): Unique username for the user.
        email (str): Unique email address for the user.
        hashed_password (str): Hashed password for secure authentication.
        is_active (bool): Indicates if the user account is active.
        is_superuser (bool): Indicates if the user has superuser privileges.
        groups (List[GroupModel]): List of groups the user belongs to.
        created_at (str): Timestamp of when the user was created.
        updated_at (str): Timestamp of the last update to the user record.

    Example:
        >>> new_user = User(
        ...     username="johndoe",
        ...     email="johndoe@example.com",
        ...     hashed_password="hashedpassword123",
        ...     is_active=True,
        ...     is_superuser=False
        ... )
        >>> session.add(new_user)
        >>> session.commit()
    """


    __tablename__ = "user"
    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[str] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[str] = mapped_column(init=False, server_default=func.now(), onupdate=func.now())

    groups = relationship("Group", secondary="user_groups", back_populates="users")