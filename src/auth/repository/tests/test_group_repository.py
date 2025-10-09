from sqlalchemy import select
from auth.model import Group


def test_get_by_id(create_group, group_repository):
    id = 1
    stmt = group_repository.get_by_id(id)
    assert stmt is not None

def test_get_by_name(create_group, group_repository):
    stmt = group_repository.get_by_name("testgroup")
    assert stmt is not None

def test_create_group(session, group_repository):
    new_group = Group(
        name="newgroup",
        description="A new group"
    )

    new_group = group_repository.create(new_group)
    stmt = select(Group).where(Group.name == "newgroup")
    record = session.execute(stmt).scalar_one_or_none()
    assert record is not None

def test_update_group(session, create_group, group_repository):
    id = 1
    stmt = select(Group).where(Group.id == 1)
    record = session.execute(stmt).scalar_one_or_none()
    record.description = "An updated test group"
    group_repository.update(record)
    record_updated = session.execute(stmt).scalar_one_or_none()
    assert record_updated.description == "An updated test group"

def test_delete_group(session, create_group, group_repository):
    id = 1
    stmt = select(Group).where(Group.id == 1)
    record = session.execute(stmt).scalar_one_or_none()
    group_repository.delete(record)
    record_deleted = session.execute(stmt).scalar_one_or_none()
    assert record_deleted is None

def test_add_user_to_group(session, create_user, create_group, group_repository):
    stmt = select(Group).where(Group.id == 1)
    record = session.execute(stmt).scalar_one_or_none()
    group_repository.add_user(record, 1)
    record_with_user = session.execute(stmt).scalar_one_or_none()
    assert len(record_with_user.users) == 1

def test_add_permission_to_group(session, create_group, create_permission, group_repository):
    stmt = select(Group).where(Group.id == 1)
    record = session.execute(stmt).scalar_one_or_none()
    group_repository.add_permission(record, 1)
    record_with_permission = session.execute(stmt).scalar_one_or_none()
    assert len(record_with_permission.permissions) == 1