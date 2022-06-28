from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Uplaod():
    def file_uplaod(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/upload')
        print('Test URL open success.')

        upload_button = driver.find_element(By.ID, 'file-upload')
        upload_button.send_keys('C:\\Users\\Asus\\Downloads\\image.jpg')
        time.sleep(5)

        driver.close()


testObj = Uplaod()
testObj.file_uplaod()