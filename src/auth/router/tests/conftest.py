import pytest
from fastapi import FastAPI
from utils.security import Criptografy
from fastapi.testclient import TestClient
from auth.model import User, Group, Permission
from auth.router import auth_router, auth_group_router, auth_permission_router, authentication_router
from database import create_session
from utils.mocks import create_session as mock_create_session


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
        hashed_password=password_hashed
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
        hashed_password=password_hashed
    )
    group = Group(name="testgroup", description="A test group")
    session.add(group)
    session.add(new_user)
    permission01 = Permission(name="create:user", description="Permission to create user")
    permission02 = Permission(name="delete:user", description="Permission to delete user")
    permission03 = Permission(name="update:user", description="Permission to update user")
    permission04 = Permission(name="view:user", description="Permission to view user")
    permission05 = Permission(name="add_user_to_group:user", description="Permission to add user to group")
    permission06 = Permission(name="create:group", description="Permission to create group")
    permission07 = Permission(name="delete:group", description="Permission to delete group")
    permission08 = Permission(name="update:group", description="Permission to update group")
    permission09 = Permission(name="view:group", description="Permission to view group")
    permission10 = Permission(name="add_permission_to_group:group", description="Permission to add permission to group")
    permission11 = Permission(name="add_user_to_group:group", description="Permission to add user to group")
    permission12 = Permission(name="create:permission", description="Permission to create permission")
    permission13 = Permission(name="delete:permission", description="Permission to delete permission")
    permission14 = Permission(name="view:permission", description="Permission to view permission")
    permission15 = Permission(name="update:permission", description="Permission to update permission")
    group.permissions.append(permission01)
    group.permissions.append(permission02)
    group.permissions.append(permission03)
    group.permissions.append(permission04)
    group.permissions.append(permission05)
    group.permissions.append(permission06)
    group.permissions.append(permission07)
    group.permissions.append(permission08)
    group.permissions.append(permission09)
    group.permissions.append(permission10)
    group.permissions.append(permission11)
    group.permissions.append(permission12)
    group.permissions.append(permission13)
    group.permissions.append(permission14)
    group.permissions.append(permission15)
    session.add(permission01)
    session.add(permission02)
    session.add(permission03)
    session.add(permission04)
    session.add(permission05)
    session.add(permission06)
    session.add(permission07)
    session.add(permission08)
    session.add(permission09)
    session.add(permission10)
    session.add(permission11)
    session.add(permission12)
    session.add(permission13)
    session.add(permission14)
    session.add(permission15)
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
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json().get("access_token")

@pytest.fixture
def create_token_user_common(client) -> str:
    response = client.post(
        "/login",
        data={"username": "testuser", "password": "testpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json().get("access_token")