from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Type():

    def weblement_type(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Test URL open success.')

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
        print('password typing: '+ password_data)
        login_btn.click()
        print('Login Button clicked.')
        time.sleep(5)

        driver.close()
        print("Test Complete.Browser closed.")


test_obj = Type()
test_obj.weblement_type()
