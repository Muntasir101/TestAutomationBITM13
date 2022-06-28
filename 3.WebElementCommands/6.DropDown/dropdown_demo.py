from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

class Dropdown():
    def dropdown_verify(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/dropdown')
        print('Test URL open success.')

        dropdown = driver.find_element(By.ID, 'dropdown')
        dropdown_options = Select(dropdown)
       # dropdown_options.select_by_value('1')
        #dropdown_options.select_by_index(2)
        dropdown_options.select_by_visible_text('Option 1')
        time.sleep(5)


testObj = Dropdown()
testObj.dropdown_verify()