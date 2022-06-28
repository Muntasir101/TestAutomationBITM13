from selenium import webdriver

class Edge_config():
    def edge_test(self):
        driver = webdriver.Edge(executable_path="E:\BITM13\Projects\TestAutomationBITM13\BrowserDrivers\msedgedriver.exe")

        driver.get('https://google.com')

test_obj = Edge_config()
test_obj.edge_test()