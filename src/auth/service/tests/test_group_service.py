import pytest
from fastapi.exceptions import HTTPException


def test_get_group_by_id(session, group_service, create_group):
    group_id = 1
    group = group_service.get_group_by_id(group_id)
    assert group is not None


def test_get_group_by_name(session, group_service, create_group):
    name = "testgroup"
    group = group_service.get_group_by_name(name)
    assert group is not None


def test_create_group(session, group_service):
    group_data = {
        "name": "newgroup",
        "description": "A new test group",
    }
    group = group_service.create_group(group_data)
    assert group is not None
    assert group.name == "newgroup"


def test_create_group_existing_name(session, group_service, create_group):
    group_data = {
        "name": "testgroup",
        "description": "Another test group",
    }

    with pytest.raises(HTTPException) as exc_info:
        group_service.create_group(group_data)

    assert exc_info.value.detail == "Group already exists"


def test_update_group(session, group_service, create_group):
    group_id = 1
    group_data = {
        "name": "updatedgroup",
        "description": "An updated test group",
    }
    group = group_service.update_group(group_id, group_data)
    assert group is not None
    assert group.name == "updatedgroup"


def test_delete_group(session, group_service, create_group):
    group_id = 1
    result = group_service.delete_group(group_id)
    assert result == {"detail": "Group deleted successfully"}


def test_add_permission_to_group(session, group_service, create_group, create_permission):
    group_id = 1
    permission_id = 1
    result = group_service.add_permission_to_group(group_id, permission_id)
    assert result is not None


def test_add_user_to_group(session, group_service, create_group, create_user):
    group_id = 1
    user_id = 1
    result = group_service.add_user_to_group(group_id, user_id)
    assert result is not None
