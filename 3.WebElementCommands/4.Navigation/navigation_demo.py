from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Navigation():
    def navigation_check(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Test URL open success.')

        # navigate to google
        driver.get("https:google.com")
        time.sleep(3)

        # Back to OrangeHRM
        driver.back()
        time.sleep(3)

        # Forward to Google
        driver.forward()
        time.sleep(3)

        # Back to OrangeHRM
        driver.back()

        username = driver.find_element(By.ID, 'txtUsername')

        username_display_status = username.is_displayed()
        username_enable_status = username.is_enabled()

        if username_display_status == True and username_enable_status == True:
            username.send_keys("Admin this is very important")
            print("Username Typed")
            time.sleep(5)

        else:
            print("Element not Active.Bug found.")

        # Refresh
        driver.refresh()
        time.sleep(2)

        driver.close()


testObj = Navigation()
testObj.navigation_check()




