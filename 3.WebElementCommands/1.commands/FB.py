from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class FB_Test():

    def fb_login_tc001(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.facebook.com/')
        print('Test URL open success.')

        email = driver.find_element(By.ID, 'email')

        # Password
        password = driver.find_element(By.ID, 'pass')

        # Login Button
        login_btn = driver.find_element(By.NAME, 'login')

        username_data = 'Admin'
        password_data = 'admin123'

        email.send_keys(username_data)
        time.sleep(2)
        print("Username Typing: " + username_data)

        password.send_keys(password_data)
        time.sleep(2)
        print('password typing: ' + password_data)

        login_btn.click()
        print('Login Button clicked.')
        time.sleep(5)

        driver.close()
        print("Test Complete.Browser closed.")

    def fb_login_tc002(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.facebook.com/')
        print('Test URL open success.')

        email = driver.find_element(By.ID, 'email')

        # Password
        password = driver.find_element(By.ID, 'pass')

        # Login Button
        login_btn = driver.find_element(By.NAME, 'login')

        username_data = 'Admin2'
        password_data = 'admin123efed'

        email.send_keys(username_data)
        time.sleep(2)
        print("Username Typing: " + username_data)

        password.send_keys(password_data)
        time.sleep(2)
        print('password typing: ' + password_data)

        login_btn.click()
        print('Login Button clicked.')
        time.sleep(5)

        driver.close()
        print("Test Complete.Browser closed.")

    def fb_login_tc003(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.facebook.com/')
        print('Test URL open success.')

        # Email
        email = driver.find_element(By.ID, 'email')

        # Password
        password = driver.find_element(By.ID, 'pass')

        # Login Button
        login_btn = driver.find_element(By.NAME, 'login')

        username_data = 'Admin2adawd'
        password_data = 'admin123efedsadsad'

        email.send_keys(username_data)
        time.sleep(2)
        print("Username Typing: " + username_data)

        password.send_keys(password_data)
        time.sleep(2)
        print('password typing: ' + password_data)

        login_btn.click()
        print('Login Button clicked.')
        time.sleep(5)

        driver.close()
        print("Test Complete.Browser closed.")


test_obj = FB_Test()
test_obj.fb_login_tc001()
#test_obj.fb_login_tc002()
#test_obj.fb_login_tc003()
