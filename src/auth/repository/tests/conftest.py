import pytest
from utils.mocks import create_session
from auth.model import User, Group, Permission
from auth.repository import UserRepository, GroupRepository, PermissionRepository


@pytest.fixture
def session():
    _session = create_session()
    return _session.__next__()

@pytest.fixture
def user_repository(session) -> UserRepository:
    return UserRepository(session)

@pytest.fixture
def group_repository(session) -> UserRepository:
    return GroupRepository(session)

@pytest.fixture
def permission_repository(session) -> PermissionRepository:
    return PermissionRepository(session)

@pytest.fixture
def create_user(session, user_repository) -> None:
    new_user = User(
        username="testuser", 
        email="testuser@example.com",
        hashed_password="testpassword"
    )

    session.add(new_user)
    session.commit()

@pytest.fixture
def create_permission(session, permission_repository) -> None:
    new_permission = Permission(
        name="testpermission", 
        description="A test permission"
    )

    session.add(new_permission)
    session.commit()

@pytest.fixture
def create_group(session) -> None:
    new_group = Group(
        name="testgroup", 
        description="A test group"
    )

    session.add(new_group)
    session.commit()