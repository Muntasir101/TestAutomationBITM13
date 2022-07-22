import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def browser_config():
    global driver

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print('Browser launch success.')
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    print('Test URL open success.')

    yield
    driver.close()
    print("Test Complete.Browser closed.")

def test_login_valid(browser_config):
    # Username
    username = driver.find_element(By.ID, 'txtUsername')

    # Password
    password = driver.find_element(By.XPATH, '//*[@id="txtPassword"]')

    # Login Button
    login_btn = driver.find_element(By.ID, 'btnLogin')

    username_data = 'Admin'
    password_data = 'admin123'

    username.send_keys(username_data)
    print("Username Typing: " + username_data)
    password.send_keys(password_data)
    print('password typing: ' + password_data)
    login_btn.click()
    print('Login Button clicked.')
    time.sleep(5)


def test_login_invalid(browser_config):
    # Username
    username = driver.find_element(By.ID, 'txtUsername')

    # Password
    password = driver.find_element(By.XPATH, '//*[@id="txtPassword"]')

    # Login Button
    login_btn = driver.find_element(By.ID, 'btnLogin')

    username_data = 'Admininvalid'
    password_data = 'admin123'

    username.send_keys(username_data)
    print("Username Typing: " + username_data)
    password.send_keys(password_data)
    print('password typing: ' + password_data)
    login_btn.click()
    print('Login Button clicked.')
    time.sleep(5)
