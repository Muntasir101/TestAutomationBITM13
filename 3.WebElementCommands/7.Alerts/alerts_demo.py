from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Alert():
    def all_type_alert(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/javascript_alerts')
        print('Test URL open success.')

        # Normal alert
        normal_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
        normal_alert.click()
        time.sleep(4)

        # Move to alert
        driver.switch_to.alert.accept()  # click on OK
        print('Normal Alert Accept')

        # Confirm alert
        confirm_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
        confirm_alert.click()
        time.sleep(4)

        # move to alert
        driver.switch_to.alert.dismiss()  # click on cancel
        time.sleep(4)
        print('Confirm Alert Cancel')

        # Prompt alert
        prompt_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
        prompt_alert.click()
        time.sleep(4)

        # move to alert
        driver.switch_to.alert.send_keys('Test Automation.')  # Type on alert input field
        driver.switch_to.alert.accept()
        print('Type on Prompt alert done.')
        time.sleep(4)

        driver.close()


test_obj = Alert()
test_obj.all_type_alert()
