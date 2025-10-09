def test_get_group_by_id(session, group_service, create_group):
    id = 1
    group = group_service.get_group_by_id(id)
    assert group is not None

def test_get_group_by_name(session, group_service, create_group):
    name = "testgroup"
    group = group_service.get_group_by_name(name)
    assert group is not None

def test_create_group(session, group_service):
    group_data = {
        "name": "newgroup",
        "description": "A new test group"
    }
    group = group_service.create_group(group_data)
    assert group is not None
    assert group.name == "newgroup"

def test_create_group_existing_name(session, group_service, create_group):
    group_data = {
        "name": "testgroup",
        "description": "Another test group"
    }
    group = group_service.create_group(group_data)
    assert group is None

def test_update_group(session, group_service, create_group):
    id = 1
    group_data = {
        "name": "updatedgroup",
        "description": "An updated test group"
    }
    group = group_service.update_group(id, group_data)
    assert group is not None
    assert group.name == "updatedgroup"

def test_delete_group(session, group_service, create_group):
    id = 1
    result = group_service.delete_group(id)
    assert result is True
