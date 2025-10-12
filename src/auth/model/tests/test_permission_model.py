import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from auth.model import Permission


def test_create_permission(session):
    data = {
        "name": "testpermission",
        "description": "A test permission",
    }

    new_permission = Permission(**data)
    session.add(new_permission)
    session.commit()
    stmt = select(Permission).where(Permission.name == "testpermission")
    result = session.execute(stmt).scalars().first()
    assert result is not None
    assert result.name == "testpermission"
    assert result.description == "A test permission"


def test_constraints_unique_permission_name(session):
    data1 = {
        "name": "testpermission",
        "description": "A test permission",
    }

    data2 = {
        "name": "testpermission",
        "description": "Another test permission",
    }

    new_permission1 = Permission(**data1)
    new_permission2 = Permission(**data2)
    session.add(new_permission1)
    session.add(new_permission2)

    with pytest.raises(IntegrityError) as exc_info:
        session.commit()

    assert "UNIQUE constraint failed: permission.name" in str(exc_info.value)
