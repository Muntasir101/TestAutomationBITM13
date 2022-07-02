from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Screenshot_demo():

    def capture_screenshot(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Test URL open success.')

        driver.save_screenshot("E:\\BITM13\Projects\\TestAutomationBITM13\\ScreenshotFiles\\orange.png")
        print('Screenshot Capture Successful')

        driver.close()


obj = Screenshot_demo()
obj.capture_screenshot()