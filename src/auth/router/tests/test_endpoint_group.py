from fastapi import status


def test_create_group(client, create_user_with_group, create_token_admin):
    response = client.post(
        "/groups/",
        headers={"Authorization": f"Bearer {create_token_admin}"},
        json={
            "name": "test_group",
            "description": "A group for testing",
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "test_group",
        "description": "A group for testing",
    }


def test_create_group_without_permission_expects_error(client, create_user, create_token_user_common):
    response = client.post(
        "/groups/",
        headers={"Authorization": f"Bearer {create_token_user_common}"},
        json={
            "name": "test_group",
            "description": "A group for testing",
        },
    )

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Not authorized"}


def test_create_when_group_exists_expects_error(client, create_group, create_user_with_group, create_token_admin):
    response = client.post(
        "/groups/",
        headers={"Authorization": f"Bearer {create_token_admin}"},
        json={
            "name": "testgroup",
            "description": "A test group",
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Group already exists"}


def test_delete_group_expects_not_found(client, create_group, create_user_with_group, create_token_admin):
    response = client.delete("/groups/999", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Group not found"}


def test_delete_group_expects_success(client, create_group, create_user_with_group, create_token_admin):
    response = client.delete("/groups/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"detail": "Group deleted successfully"}


def test_update_partial_fields_group_expects_success(client, create_group, create_user_with_group, create_token_admin):
    response = client.put(
        "/groups/1",
        json={
            "description": "An updated test group",
        },
        headers={"Authorization": f"Bearer {create_token_admin}"},
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "secondgroup",
        "description": "An updated test group",
    }


def test_update_when_group_not_exists_expects_error(client, create_user_with_group, create_token_admin):
    response = client.put(
        "/groups/999",
        json={
            "name": "updatedgroup",
            "description": "An updated test group",
        },
        headers={"Authorization": f"Bearer {create_token_admin}"},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Group not found"}


def test_get_group_by_id_expects_success(client, create_group, create_user_with_group, create_token_admin):
    response = client.get("/groups/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": "secondgroup",
        "description": "A test group",
    }


def test_get_user_by_id_not_found_expects_error(client, create_user_with_group, create_token_admin):
    response = client.get("/groups/999", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Group not found"}


def test_add_user_to_group_expects_success(
    client,
    create_user,
    create_group,
    create_user_with_group,
    create_token_admin,
):
    response = client.post("/group/1/user/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"detail": "User added to group successfully"}


def test_add_user_to_group_not_found_expects_error(client, create_user_with_group, create_token_admin):
    response = client.post("/group/999/user/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User or Group not found"}


def test_add_permission_to_group_expects_success(
    client,
    create_user,
    create_group,
    create_user_with_group,
    create_token_admin,
):
    response = client.post("/group/1/permission/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"detail": "Permission added to group successfully"}


def test_add_permission_to_group_not_found_expects_error(client, create_user_with_group, create_token_admin):
    response = client.post("/group/999/permission/1", headers={"Authorization": f"Bearer {create_token_admin}"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Permission or Group not found"}
