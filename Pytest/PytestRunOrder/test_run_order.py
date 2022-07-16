import pytest

@pytest.mark.order(3)
def test_login_valid_001():
    print("Login with Valid data test DONE")

@pytest.mark.order(2)
def test_login_invalid_002():
    print("Login with InValid data test DONE")

@pytest.mark.order(1)
def test_login_invalid_important_003():
    print("Login test DONE")