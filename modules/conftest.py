import pytest
@pytest.fixture()
def setup():
    print("launching code")
    yield
    print("ending code")