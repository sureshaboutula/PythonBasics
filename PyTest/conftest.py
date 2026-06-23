import pytest

@pytest.fixture(scope = "function")
def pre_setup_work():
    print("I setup browser instance")