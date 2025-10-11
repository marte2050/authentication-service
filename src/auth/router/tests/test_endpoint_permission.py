def test_create_permission(client, create_user_with_group, create_token_admin):
    response = client.post(
        "/permissions/",
        json={"name": "read_articles", "description": "Permission to read articles"},
        headers={"Authorization": f"Bearer {create_token_admin}"}
    )
    assert response.status_code == 200
    assert response.json() == {
        'name': 'read_articles', 
        'description': 'Permission to read articles'
    }

def test_create_when_exists_permission(client, create_permission, create_user_with_group, create_token_admin):
    response = client.post(
        "/permissions/",
        json={"name": "testpermission", "description": "A test permission"},
        headers={"Authorization": f"Bearer {create_token_admin}"}
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Permission with this name already exists."
    }

def test_delete_permission(client, create_permission, create_user_with_group, create_token_admin):
    response = client.delete("/permissions/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == 200
    assert response.json() == {"detail": "Permission deleted successfully."}

def test_delete_nonexistent_permission(client, create_permission, create_user_with_group, create_token_admin):
    response = client.delete("/permissions/999", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Permission not found."}

def test_get_permission_by_id(client, create_permission, create_user_with_group, create_token_admin):
    response = client.get("/permissions/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == 200
    assert response.json() == {
        'name': 'testpermission', 
        'description': 'A test permission'
    }

def test_get_nonexistent_permission_by_id(client, create_permission, create_user_with_group, create_token_admin):
    response = client.get("/permissions/999", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Permission not found."}

def test_update_permission(client, create_permission, create_user_with_group, create_token_admin):
    response = client.put(
        "/permissions/1",
        json={"name": "updated_permission", "description": "Updated description"},
        headers={"Authorization": f"Bearer {create_token_admin}"}
    )
    assert response.status_code == 200
    assert response.json() == {
        'name': 'updated_permission', 
        'description': 'Updated description'
    }

def test_update_nonexistent_permission(client, create_permission, create_user_with_group, create_token_admin):
    response = client.put(
        "/permissions/999",
        json={"name": "nonexistent_permission", "description": "Should not exist"},
        headers={"Authorization": f"Bearer {create_token_admin}"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Permission not found."}