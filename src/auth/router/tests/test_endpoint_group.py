def test_create_group(client):
    response = client.post(
        "/groups/",
        json={
            "name": "test_group", 
            "description": "A group for testing"
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "name": "test_group",
        "description": "A group for testing",
    }

def test_create_when_group_exists_expects_error(client, create_group):
    response = client.post(
        "/groups/",
        json={
            "name": "testgroup", 
            "description": "A test group"
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail":"Group already exists"}

def test_delete_group_expects_not_found(client):
    response = client.delete("/groups/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Group not found"}

def test_delete_group_expects_success(client, create_group):
    response = client.delete("/groups/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Group deleted successfully"}

def test_update_partial_fields_group_expects_success(client, create_group):
    response = client.put(
        "/groups/1",
        json={
            "description": "An updated test group"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "testgroup",
        "description": "An updated test group"
    }

def test_update_when_group_not_exists_expects_error(client):
    response = client.put(
        "/groups/1",
        json={
            "name": "updatedgroup",
            "description": "An updated test group"
        }
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Group not found"}

def test_get_user_by_id_expects_success(client, create_group):
    response = client.get("/groups/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "testgroup",
        "description": "A test group"
    }

def test_get_user_by_id_not_found_expects_error(client):
    response = client.get("/groups/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Group not found"}

def test_add_user_to_group_expects_success(client, create_user, create_group):
    response = client.post("/group/1/group/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "User added to group successfully"}

def test_add_user_to_group_not_found_expects_error(client):
    response = client.post("/group/1/group/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "User or Group not found"}

def test_add_permission_to_group_expects_success(client, create_group, create_permission):
    response = client.post("/group/1/permission/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Permission added to group successfully"}

def test_add_permission_to_group_not_found_expects_error(client):
    response = client.post("/group/1/permission/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Permission or Group not found"}