from fastapi import status


def test_create_user(client, create_user_with_group, create_token_admin):
    response = client.post(
        "/user/",
        headers={"Authorization": f"Bearer {create_token_admin}"},
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword",
        },
    )
    output_expected = {
        "username": "testuser",
        "email": "testuser@example.com",
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == output_expected


def test_create_user_without_permission_expects_forbidden(client, create_user, create_token_user_common):
    response = client.post(
        "/user/",
        headers={"Authorization": f"Bearer {create_token_user_common}"},
        json={
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword",
        },
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Not authorized"}


def test_delete_user_expects_not_found(client, create_user_with_group, create_token_admin):
    response = client.delete("/user/999", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_user_expects_success(client, create_user, create_user_with_group, create_token_admin):
    response = client.delete("/user/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"detail": "User deleted successfully"}


def test_update_when_no_user_expects_not_found(client, create_user_with_group, create_token_admin):
    response = client.put(
        "/user/999",
        json={
            "username": "updateduser",
            "email": "updateduser@example.com",
        },
        headers={"Authorization": f"Bearer {create_token_admin}"},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_update_all_fields_user_expects_success(client, create_user, create_user_with_group, create_token_admin):
    response = client.put(
        "/user/1",
        json={
            "username": "updateduser",
            "email": "updateduser@example.com",
        },
        headers={"Authorization": f"Bearer {create_token_admin}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "username": "updateduser",
        "email": "updateduser@example.com",
    }


def test_update_partial_fields_user_expects_success(client, create_user, create_user_with_group, create_token_admin):
    response = client.put(
        "/user/1",
        json={
            "email": "updateduser@example.com",
        },
        headers={"Authorization": f"Bearer {create_token_admin}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "username": "testuser",
        "email": "updateduser@example.com",
    }


def test_get_user_by_id_expects_success(client, create_user, create_user_with_group, create_token_admin):
    response = client.get("/user/1", headers={"Authorization": f"Bearer {create_token_admin}"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "username": "testuser",
        "email": "testuser@example.com",
    }


def test_get_user_by_id_expects_not_found(client, create_user, create_user_with_group, create_token_admin):
    response = client.get("/user/999", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_add_user_to_group_expects_success(client, create_user, create_user_with_group, create_token_admin):
    response = client.post("/user/1/group/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"detail": "User added to group successfully"}


def test_add_user_to_group_expects_not_found(client, create_user, create_user_with_group, create_token_admin):
    response = client.post("/user/1/group/999", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User or Group not found"}
