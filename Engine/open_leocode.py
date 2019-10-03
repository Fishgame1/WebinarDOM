import inspect

from selenium import webdriver

from Engine.main_page import MainPage


class OpenLeocode:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/home/wilk/git/AutomatedWebTests/chromedriver')
        self.driver.maximize_window()

    def __enter__(self):
        self.driver.get('https://leocode.com/')
        return MainPage(self.driver)

    def __exit__(self, _type, _value, _tb):
        self.driver.quit()
