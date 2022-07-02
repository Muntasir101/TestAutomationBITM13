from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Headless_demo():
    def headless_chrome(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        print('Browser launch success in Headless Mode')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Title is: ' + driver.title)
        print('Test Done.')

        driver.close()


obj = Headless_demo()
obj.headless_chrome()
