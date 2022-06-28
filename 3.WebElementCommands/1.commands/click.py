from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Element_click():

    def weblement_click(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Test URL open success.')

        # forgot password
        forgot_password = driver.find_element(By.LINK_TEXT, 'Forgot your password?')
        forgot_password.click()
        print("Forgot password page open.")
        time.sleep(5)

        driver.close()
        print('Browser close Success.')


test_obj = Element_click()
test_obj.weblement_click()
