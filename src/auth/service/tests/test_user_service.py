import pytest
from fastapi.exceptions import HTTPException

def test_get_user_by_id(user_service,create_user):
    id = 1
    user = user_service.get_user_by_id(id)
    assert user is not None
    
def test_get_user_by_username(user_service,create_user):
    username = "testuser"
    user = user_service.get_user_by_username(username)
    assert user is not None

def test_get_user_by_email(user_service,create_user):
    email = "testuser@example.com"
    user = user_service.get_user_by_email(email)
    assert user is not None

def test_create_user(user_service):
    user_data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "password"
    }

    user = user_service.create_user(user_data)
    assert user is not None

def test_create_user_existing_username(user_service, create_user):
    user_data = {
        "username": "testuser",  # Existing username
        "email": "testuser@example.com",
        "password": "password"
    }
    with pytest.raises(HTTPException) as exc_info:
        user = user_service.create_user(user_data)
    
    value = exc_info.value.detail
    assert value == "Username or email already in use"

def test_create_user_existing_email(user_service, create_user):
    user_data = {
        "username": "anotheruser",
        "email": "testuser@example.com",  # Existing email
        "password": "password"
    }

    with pytest.raises(HTTPException) as exc_info:
        user = user_service.create_user(user_data)
    
    value = exc_info.value.detail
    assert value == "Username or email already in use"

def test_update_user(user_service, create_user):
    user_id = 1
    user_data = {
        "username": "updateduser",
        "email": "updateduser@example.com",
    }

    user = user_service.update_user(user_id, user_data)
    assert user.email == "updateduser@example.com"
    assert user.username == "updateduser"

def test_delete_user(user_service, create_user):
    user = user_service.delete_user(1)
    assert user is True

def test_change_password(user_service, create_user):
    user_service.change_password(1, "newpassword")
    user = user_service.get_user_by_id(1)
    assert user.hashed_password != "testpassword"

def test_add_group_to_user(user_service, create_user, create_group):
    user_service.add_group_to_user(1, 1)
    user = user_service.get_user_by_id(1)
    assert len(user.groups) == 1