from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Element_CSS():

    def locator_css(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Test URL open success.')

        # Username
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')

        if password is not None:
            print("We found password by CSS")
        else:
            print("We dont found password by CSS")

        driver.close()
        print('Browser close Success.')


test_obj = Element_CSS()
test_obj.locator_css()