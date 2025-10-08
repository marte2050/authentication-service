import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from auth.model import Group


def test_create_group(session):
    data = {
        "name": "testgroup",
        "description": "A test group",
    }
    
    new_group = Group(**data)
    session.add(new_group)
    session.commit()
    stmt = select(Group).where(Group.name == "testgroup")
    result = session.execute(stmt).scalars().first()
    assert result is not None
    assert result.name == "testgroup"
    assert result.description == "A test group"


def test_constraints_unique_group_name(session):
    data1 = {
        "name": "testgroup",
        "description": "A test group",
    }

    data2 = {
        "name": "testgroup",
        "description": "Another test group",
    }

    new_group1 = Group(**data1)
    new_group2 = Group(**data2)

    with pytest.raises(IntegrityError) as exc_info:
        session.add(new_group1)
        session.add(new_group2)
        session.commit()

    assert "UNIQUE constraint failed: group.name" in str(exc_info.value)