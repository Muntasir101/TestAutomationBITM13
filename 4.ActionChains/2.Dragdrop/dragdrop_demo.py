from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class DragDrop():
    def drag_drop(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://jqueryui.com/droppable/')
        print('Test URL open success.')

        driver.switch_to.frame(0)

        source = driver.find_element(By.ID, 'draggable')
        target = driver.find_element(By.ID, 'droppable')

        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        time.sleep(5)


testObj = DragDrop()
testObj.drag_drop()
