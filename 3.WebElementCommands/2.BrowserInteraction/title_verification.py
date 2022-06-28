from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Title_Verify():

    def google_title(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.google.com/')
        print('Test URL open success.')

        # Get Title from current page
        actual_title = driver.title
        print('Google Title is: ' + actual_title)

        expected_title = 'Google2'

        if expected_title == actual_title:
            print("Google Title Matched.Test Passed.")
        else:
            print("Test Failed.")

        driver.close()
        print("Test Complete.Browser closed.")


test_obj = Title_Verify()
test_obj.google_title()
