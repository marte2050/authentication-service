def test_create_user(client):
    response = client.post(
        "/user/", 
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword"
        }
    )
    output_expected = {
        "username": "testuser",
        "email": "testuser@example.com",
    }
    assert response.status_code == 200
    assert response.json() == output_expected

def test_delete_user_expects_not_found(client):
    response = client.delete("/user/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_delete_user_expects_success(client, create_user):
    response = client.delete("/user/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "User deleted successfully"}

def test_update_when_no_user_expects_not_found(client):
    response = client.put(
        "/user/1",
        json={
            "username": "updateduser",
            "email": "updateduser@example.com",
        }
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_update_all_fields_user_expects_success(client, create_user):
    response = client.put(
        "/user/1",
        json={
            "username": "updateduser",
            "email": "updateduser@example.com",
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "username": "updateduser",
        "email": "updateduser@example.com"
    }

def test_update_partial_fields_user_expects_success(client, create_user):
    response = client.put(
        "/user/1",
        json={
            "email": "updateduser@example.com",
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "testuser",
        "email": "updateduser@example.com"
    }

def test_get_user_by_id_expects_success(client, create_user):
    response = client.get("/user/1")

    assert response.status_code == 200
    assert response.json() == {
        "username": "testuser",
        "email": "testuser@example.com"
    }

def test_get_user_by_id_expects_not_found(client):
    response = client.get("/user/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_add_user_to_group_expects_success(client, create_user, create_group):
    response = client.post("/user/1/group/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "User added to group successfully"}

def test_add_user_to_group_expects_not_found(client):
    response = client.post("/user/1/group/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "User or Group not found"}
