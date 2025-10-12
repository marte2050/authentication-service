from fastapi import status


def test_authentication_when_username_not_found(client):
    response = client.post(
        "/login",
        data={
            "username": "testuser",
            "password": "testpassword",
        },
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Invalid username or password"}


def test_authentication_when_password_incorrect(client, create_user):
    response = client.post(
        "/login",
        data={
            "username": "testuser",
            "password": "wrongpassword",
        },
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Invalid username or password"}


def test_authentication_success(client, create_user):
    response = client.post(
        "/login",
        data={
            "username": "testuser",
            "password": "testpassword",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
