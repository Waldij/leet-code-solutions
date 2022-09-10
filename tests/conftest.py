import pytest


@pytest.fixture
def mr_printer():
    print('Start fixture')
    yield
    print('End fixture')
