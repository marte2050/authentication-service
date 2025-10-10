import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from auth.model import User, Group, Permission
from auth.router import auth_router, auth_group_router, auth_permission_router
from database import create_session
from utils.mocks import create_session as mock_create_session


@pytest.fixture
def client(session):
    app = FastAPI()
    app.dependency_overrides[create_session] = lambda: session
    app.include_router(auth_router)
    app.include_router(auth_group_router)
    app.include_router(auth_permission_router)
    return TestClient(app)

@pytest.fixture
def session():
    yield from mock_create_session()

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