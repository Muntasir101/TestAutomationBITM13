from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Scrolling():
    def scroll_to_end(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.apple.com/')
        print('Test URL open success.')

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(7)

        driver.close()


obj = Scrolling()
obj.scroll_to_end()
