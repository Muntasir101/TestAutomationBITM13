from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class SwitchTab():
    def multiple_tab_switch(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/windows')
        print('Test URL open success.')

        parent_GUID = driver.current_window_handle
        # print('parent GUID: ' + parent_GUID)

        driver.find_element(By.LINK_TEXT, 'Click Here').click()

        all_GUID = driver.window_handles
        # print(all_GUID)

        # switch to child
        for child_guid in all_GUID:
            if child_guid not in parent_GUID:
                driver.switch_to.window(child_guid)
                print('After switch child Tab : ' + driver.title)

        # switch to parent
        for child_guid in all_GUID:
            if child_guid not in parent_GUID:
                driver.switch_to.window(parent_GUID)
                print('After switch parent Tab : ' + driver.title)


obj = SwitchTab()
obj.multiple_tab_switch()
