import pytest
from utils.mocks import create_session


@pytest.fixture
def session():
    yield from create_session()