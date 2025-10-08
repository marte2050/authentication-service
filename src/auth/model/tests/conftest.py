import pytest
from utils.mocks import create_session


@pytest.fixture
def session():
    _session = create_session()
    return _session.__next__()