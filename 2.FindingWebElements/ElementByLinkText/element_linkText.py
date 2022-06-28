from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Element_LinkText():

    def locator_linkText(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Test URL open success.')

        # forgot password
        forgot_password = driver.find_element(By.LINK_TEXT, 'Forgot your password?')

        if forgot_password is not None:
            print("We found forgot_password by Xpath")
            forgot_password.click()
            print("Forgot password page open.")
        else:
            print("We dont found forgot_password by Xpath")

        driver.close()
        print('Browser close Success.')


obj = Element_LinkText()
obj.locator_linkText()