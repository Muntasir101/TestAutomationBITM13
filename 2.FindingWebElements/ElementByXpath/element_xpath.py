from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Element_Xpath():

    def locator_xpath(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Test URL open success.')

        # password
        password = driver.find_element(By.XPATH, '//*[@id="txtPassword"]')

        if password is not None:
            print("We found password by Xpath")
        else:
            print("We dont found password by Xpath")

        driver.close()
        print('Browser close Success.')


test_obj = Element_Xpath()
test_obj.locator_xpath()