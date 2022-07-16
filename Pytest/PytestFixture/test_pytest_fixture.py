import pytest

@pytest.fixture()
def browser_config():
    print('Chrome Launch Successfully')

    yield
    print("Browser Closed")

def test_login_001(browser_config):
    print("Login with Valid data test DONE")

def test_login_002(browser_config):
    print("Login with InValid data test DONE")

def test_login_003(browser_config):
    print("Login test DONE")