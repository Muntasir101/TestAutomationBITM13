from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Edge_WDM_config():

    def edge_wdm_test(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

        driver.get('https://google.com')


test_obj = Edge_WDM_config()
test_obj.edge_wdm_test()