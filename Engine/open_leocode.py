import os
import time
from pathlib import Path

from selenium import webdriver

from Engine.main_page import MainPage

cwd = Path(__file__).parents[1]


class OpenLeocode:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=os.path.join(str(cwd), 'chromedriver'))
        time.sleep(1)
        self.driver.maximize_window()

    def __enter__(self):
        self.driver.get('https://leocode.com/')
        return MainPage(self.driver)

    def __exit__(self, _type, _value, _tb):
        self.driver.quit()
