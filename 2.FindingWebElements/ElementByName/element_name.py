from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Element_Name():

    def locator_name(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Test URL open success.')

        # Username
        username = driver.find_element(By.NAME, 'txtUsername')

        if username is not None:
            print("We found Username by Name")
        else:
            print("We dont found Username by Name")

        driver.close()
        print('Browser close Success.')


test_obj = Element_Name()
test_obj.locator_name()