from selenium.webdriver.chrome.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def careers(self):
        self.driver.find_element_by_css_selector('#menu-item-5279 > a').click()
        from Engine.careers import Careers
        return Careers(self.driver)

