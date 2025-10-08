from sqlalchemy import select
from auth.model import User


def test_get_by_id(create_user, user_repository):
    id = 1
    stmt = user_repository.get_by_id(id)
    assert stmt is not None

def test_get_by_username(create_user, user_repository):
    stmt = user_repository.get_by_username("testuser")
    assert stmt is not None

def test_get_by_email(create_user, user_repository):
    stmt = user_repository.get_by_email("testuser@example.com")
    assert stmt is not None

def test_create_user(session, user_repository):
    new_user = User(
        username="newuser",
        email="user@example.com",
        hashed_password="password"
    )

    new_user = user_repository.create(new_user)
    stmt = select(User).where(User.username == "newuser")
    record = session.execute(stmt).scalar_one_or_none()
    assert record is not None

def test_update_user(session, create_user, user_repository):
    id = 1
    stmt = select(User).where(User.id == id)
    record = session.execute(stmt).scalar_one_or_none()
    record.email = "new-email@example.com"
    record.username = "updateduser"
    user_repository.update(record)
    record_updated = session.execute(stmt).scalar_one_or_none()
    assert record_updated.email == "new-email@example.com"
    assert record_updated.username == "updateduser"

def test_delete_user(session, create_user, user_repository):
    id = 1
    stmt = select(User).where(User.id == id)
    record = session.execute(stmt).scalar_one_or_none()
    user_repository.delete(record)
    record_deleted = session.execute(stmt).scalar_one_or_none()
    assert record_deleted is None

def test_add_group(session, create_group, create_user, user_repository):
    id = 1
    stmt = select(User).where(User.id == id)
    record = session.execute(stmt).scalar_one_or_none()
    user_repository.add_group(record, 1)
    record_with_group = session.execute(stmt).scalar_one_or_none()
    assert len(record_with_group.groups) == 1