from selenium import webdriver


class Chrome_config():
    def chrome_test(self):
        driver = webdriver.Chrome(
            executable_path="E:\BITM13\Projects\TestAutomationBITM13\BrowserDrivers\chromedriver.exe")

        driver.get('https://google.com')


test_obj = Chrome_config()
test_obj.chrome_test()
