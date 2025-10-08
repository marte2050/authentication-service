import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from auth.model.user import User


def test_create_user(session):
    data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "hashed_password": "hashedpassword",
        "is_active": True,
        "is_superuser": False
    }
    
    new_user = User(**data)
    session.add(new_user)
    session.commit()
    stmt = select(User).where(User.username == "testuser")
    result = session.execute(stmt).scalars().first()
    assert result is not None
    assert result.username == "testuser"
    assert result.hashed_password == "hashedpassword"
    assert result.is_active is True
    assert result.is_superuser is False
    assert result.email == "testuser@example.com"


def test_constraints_unique_username(session):
    data1 = {
        "username": "testuser",
        "email": "testuser@example.com",
        "hashed_password": "hashedpassword",
        "is_active": True,
        "is_superuser": False
    }

    data2 = {
        "username": "testuser",
        "email": "other@example.com",
        "hashed_password": "hashedpassword",
        "is_active": True,
        "is_superuser": False
    }
    
    new_user1 = User(**data1)
    new_user2 = User(**data2)

    with pytest.raises(IntegrityError) as exc_info:
        session.add(new_user1)
        session.add(new_user2)
        session.commit()

    assert "UNIQUE constraint failed: user.username" in str(exc_info.value)

def test_constraints_unique_email(session):
    data1 = {
        "username": "testuser1",
        "email": "testuser@example.com",
        "hashed_password": "hashedpassword",
        "is_active": True,
        "is_superuser": False
    }

    data2 = {
        "username": "testuser2",
        "email": "testuser@example.com",
        "hashed_password": "hashedpassword",
        "is_active": True,
        "is_superuser": False
    }
    
    new_user1 = User(**data1)
    new_user2 = User(**data2)

    with pytest.raises(IntegrityError) as exc_info:
        session.add(new_user1)
        session.add(new_user2)
        session.commit()

    assert "UNIQUE constraint failed: user.email" in str(exc_info.value)