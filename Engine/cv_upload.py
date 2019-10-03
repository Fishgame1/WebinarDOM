from selenium.webdriver.chrome.webdriver import WebDriver


class CVUpload:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def write_name(self, text):
        self.driver.find_element_by_xpath('//*[@class="job-offers__form"]//input[@type="text"]').send_keys(text)

    def write_email(self, text):
        self.driver.find_element_by_xpath('//*[@class="job-offers__form"]//input[@type="email"]').send_keys(text)

    def write_about_your_self(self, text):
        self.driver.find_element_by_xpath('//*[@class="job-offers__form"]//textarea').send_keys(text)

    def upload_cv(self, path):
        self.driver.find_element_by_css_selector('*.job-offers__form input[type="file"]').send_keys(path)

    def apply(self):
        self.driver.find_element_by_xpath('//*[@class="job-offers__form"]//input[@type="submit"]').click()
