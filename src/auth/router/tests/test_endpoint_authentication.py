def test_authentication_when_username_not_found(client):
    response = client.post(
        "/login",
        data={
            "username": "testuser",
            "password": "testpassword",
        },
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid username or password"}


def test_authentication_when_password_incorrect(client, create_user):
    response = client.post(
        "/login",
        data={
            "username": "testuser",
            "password": "wrongpassword",
        },
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid username or password"}


def test_authentication_success(client, create_user):
    response = client.post(
        "/login",
        data={
            "username": "testuser",
            "password": "testpassword",
        },
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
