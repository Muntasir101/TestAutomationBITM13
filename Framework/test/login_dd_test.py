import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Framework.pages.login_page import LoginPage
from Framework.utils import excel_utils


class LoginTest(unittest.TestCase):

    def test_login(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        # Excel implementation
        data_file = 'E:\BITM13\Projects\TestAutomationBITM13\Framework\data\login_data.xlsx'
        sheet_name = 'Sheet1'

        number_of_rows = excel_utils.get_row_count(data_file, sheet_name)

        for r in range(2, number_of_rows + 1):
            email = excel_utils.read_data(data_file, sheet_name, r, 1)
            password = excel_utils.read_data(data_file, sheet_name, r, 2)

            lp = LoginPage(driver)
            lp.login_orange(email, password)

        driver.close()
