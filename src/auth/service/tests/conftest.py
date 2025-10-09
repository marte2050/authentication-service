import pytest
from auth.model import User, Group, Permission
from auth.service import UserService, GroupService, PermissionService
from auth.repository import UserRepository, GroupRepository, PermissionRepository
from utils.mocks import create_session
from utils.security import Criptografy


@pytest.fixture
def session():
    yield from create_session()

@pytest.fixture
def user_service(session) -> UserService:
    return UserService(session, UserRepository, GroupRepository, Criptografy)

@pytest.fixture
def group_service(session) -> GroupService:
    return GroupService(session, GroupRepository, PermissionRepository)

@pytest.fixture
def permission_service(session) -> None:
    return PermissionService(session, PermissionRepository, GroupRepository)

@pytest.fixture
def create_user(session) -> None:
    new_user = User(
        username="testuser", 
        email="testuser@example.com",
        hashed_password="testpassword"
    )
    session.add(new_user)
    session.commit()

@pytest.fixture
def create_group(session) -> None:
    new_group = Group(name="testgroup", description="A test group")
    session.add(new_group)
    session.commit()

@pytest.fixture
def create_permission(session) -> None:
    new_permission = Permission(name="testpermission", description="A test permission")
    session.add(new_permission)
    session.commit()