from selenium.webdriver.chrome.webdriver import WebDriver


class Careers:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_job_offer_by_title(self, title):
        return JobOffer(self.driver, xpath=''.format(title))

    def get_job_offer_by_number(self, number):
        return JobOffer(self.driver, selector='[class="l-items"] > div:nth-child({})'.format(number))

    def _get_job_offer(self):
        pass

    def see_all(self):
        self.driver.find_element_by_css_selector('div > a[href="https://leocode.com/job-offers/').click()


class JobOffer:
    def __init__(self, driver: WebDriver, xpath=None, selector=None):
        self.xpath = xpath
        self.driver = driver
        self.selector = selector

    def get_city(self):
        pass

    def get_description(self):
        pass

    def get_salary(self):
        pass

    def get_title(self):
        pass

    def apply(self):
        if self.xpath:
            self.driver.find_element_by_xpath(self.xpath + '').click()
        else:
            self.driver.find_element_by_css_selector(self.selector + ' [class="link-overall"]').click()
        from Engine.cv_upload import CVUpload
        return CVUpload(self.driver)

