import pytest
@pytest.fixture()
def setup(self):
    print("launching code")
    yield
    print("ending code")