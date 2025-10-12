import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from auth.model import Group, Permission, User
from auth.router import auth_group_router, auth_permission_router, auth_router, authentication_router
from database import create_session
from utils.mocks import create_session as mock_create_session
from utils.security import Criptografy


@pytest.fixture
def client(session):
    app = FastAPI()
    app.dependency_overrides[create_session] = lambda: session
    app.include_router(auth_router)
    app.include_router(auth_group_router)
    app.include_router(auth_permission_router)
    app.include_router(authentication_router)
    return TestClient(app)


@pytest.fixture
def session():
    yield from mock_create_session()


@pytest.fixture
def create_user(session) -> None:
    criptografy = Criptografy()
    password_hashed = criptografy.hash_password("testpassword")
    new_user = User(
        username="testuser",
        email="testuser@example.com",
        hashed_password=password_hashed,
    )
    session.add(new_user)
    session.commit()


@pytest.fixture
def create_user_with_group(session, create_group) -> None:
    criptografy = Criptografy()
    password_hashed = criptografy.hash_password("adminpassword")
    new_user = User(
        username="adminuser",
        email="adminuser@example.com",
        hashed_password=password_hashed,
    )
    group = Group(name="testgroup", description="A test group")
    session.add(group)
    session.add(new_user)

    permissions_data = [
        ("create:user", "Permission to create user"),
        ("delete:user", "Permission to delete user"),
        ("update:user", "Permission to update user"),
        ("view:user", "Permission to view user"),
        ("add_user_to_group:user", "Permission to add user to group"),
        ("create:group", "Permission to create group"),
        ("delete:group", "Permission to delete group"),
        ("update:group", "Permission to update group"),
        ("view:group", "Permission to view group"),
        ("add_permission_to_group:group", "Permission to add permission to group"),
        ("add_user_to_group:group", "Permission to add user to group"),
        ("create:permission", "Permission to create permission"),
        ("delete:permission", "Permission to delete permission"),
        ("view:permission", "Permission to view permission"),
        ("update:permission", "Permission to update permission"),
    ]

    permissions = [Permission(name=name, description=desc) for name, desc in permissions_data]
    session.add_all(permissions)
    group.permissions.extend(permissions)

    new_user.groups.append(group)
    session.commit()


@pytest.fixture
def create_group(session) -> None:
    group = Group(name="secondgroup", description="A test group")
    session.add(group)
    session.commit()


@pytest.fixture
def create_permission(session) -> None:
    new_permission = Permission(name="testpermission", description="A test permission")
    session.add(new_permission)
    session.commit()
    return new_permission.id


@pytest.fixture
def create_token_admin(client) -> str:
    response = client.post(
        "/login",
        data={"username": "adminuser", "password": "adminpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    return response.json().get("access_token")


@pytest.fixture
def create_token_user_common(client) -> str:
    response = client.post(
        "/login",
        data={"username": "testuser", "password": "testpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    return response.json().get("access_token")
