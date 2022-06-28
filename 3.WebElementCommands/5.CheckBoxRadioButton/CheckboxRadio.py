from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Checkbox_Radio():
    def checkbox_radio_verify(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://demo.opencart.com/index.php?route=account/register&language=en-gb')
        print('Test URL open success.')

        # check 1: Newsletter radio button default "No"
        newsletter_no = driver.find_element(By.ID, 'input-newsletter-no')
        newsletter_no_actual_status = newsletter_no.is_selected()
        newsletter_no_expected_status = True

        if newsletter_no_expected_status == newsletter_no_actual_status:
            print("Default 'No' selected. Test pass.")
        else:
            print("Default 'No' unselected.Bug found.")

        # check 2: click Newsletter radio button 'Yes'
        newsletter_yes = driver.find_element(By.XPATH, '//*[@id="input-newsletter-yes"]')
        newsletter_yes.click()
        time.sleep(3)

        # check 3: Yes selected or not
        newsletter_yes_actual_status = newsletter_yes.is_selected()
        newsletter_yes_expected_status = True

        if newsletter_yes_expected_status == newsletter_yes_actual_status:
            print("'Yes' selected. Test pass.")
        else:
            print("Test Failed.Bug found.")

        driver.close()


testObj = Checkbox_Radio()
testObj.checkbox_radio_verify()
