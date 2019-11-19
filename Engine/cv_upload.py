from selenium.webdriver.chrome.webdriver import WebDriver


class CVUpload:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def write_name(self, text):
        self.driver.find_element_by_xpath('//input[@name="user_first_name"]').send_keys(text)

    def write_last_name(self, text):
        self.driver.find_element_by_xpath('//input[@name="user_last_name"]').send_keys(text)

    def write_email(self, text):
        self.driver.find_element_by_xpath('//*[@type="email"]').send_keys(text)

    def write_phone(self, text):
        self.driver.find_element_by_xpath('//input[@name="user_phone"]').send_keys(text)

    def upload_cv(self, path):
        self.driver.find_element_by_css_selector('[type="file"]').send_keys(path)

    def apply(self):
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
