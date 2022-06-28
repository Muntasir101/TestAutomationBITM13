from selenium import webdriver

class Firefox_config():
    def firefox_test(self):
        driver = webdriver.Firefox(executable_path="E:\BITM13\Projects\TestAutomationBITM13\BrowserDrivers\geckodriver.exe")

        driver.get('https://google.com')


test_obj = Firefox_config()
test_obj.firefox_test()