from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Element_state_demo():

    def element_status(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Test URL open success.')

        # Username
        username = driver.find_element(By.ID, 'txtUsername')

        username_display_status = username.is_displayed()
        username_enable_status = username.is_enabled()

        if username_display_status == True and username_enable_status == True:
            username.send_keys("Admin")
            print("Username Typed")
            time.sleep(5)

        else:
            print("Element not Active.Bug found.")

        driver.close()
        print("Browser Closed")


obj = Element_state_demo()
obj.element_status()
