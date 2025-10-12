from sqlalchemy import select

from auth.model import Permission


def test_get_by_id(create_permission, permission_repository):
    permission_id = 1
    stmt = permission_repository.get_by_id(permission_id)
    assert stmt is not None


def test_get_by_name(create_permission, permission_repository):
    stmt = permission_repository.get_by_name("testpermission")
    assert stmt is not None


def test_create_permission(session, permission_repository):
    new_permission = Permission(
        name="newpermission",
        description="A new permission",
    )

    new_permission = permission_repository.create(new_permission)
    stmt = select(Permission).where(Permission.name == "newpermission")
    record = session.execute(stmt).scalar_one_or_none()
    assert record is not None


def test_update_permission(session, create_permission, permission_repository):
    permission_id = 1
    stmt = select(Permission).where(Permission.id == permission_id)
    record = session.execute(stmt).scalar_one_or_none()
    record.description = "An updated test permission"
    permission_repository.update(record)
    record_updated = session.execute(stmt).scalar_one_or_none()
    assert record_updated.description == "An updated test permission"


def test_delete_permission(session, create_permission, permission_repository):
    permission_id = 1
    stmt = select(Permission).where(Permission.id == permission_id)
    record = session.execute(stmt).scalar_one_or_none()
    permission_repository.delete(record)
    record_deleted = session.execute(stmt).scalar_one_or_none()
    assert record_deleted is None


def test_add_permission_to_group(session, create_permission, create_group, permission_repository):
    permission_id = 1
    group_id = 1
    stmt = select(Permission).where(Permission.id == permission_id)
    record = session.execute(stmt).scalar_one_or_none()
    permission_repository.add_to_group(record, group_id)
    record = session.execute(stmt).scalar_one_or_none()
    assert len(record.groups) == 1
