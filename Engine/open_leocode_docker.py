from selenium import webdriver

from Engine.main_page import MainPage


class OpenLeocodeDocker:
    def __init__(self):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--window-size={},{}".format(1800, 600))
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/WebinarDOM/chromedriver')

    def __enter__(self):
        self.driver.get('https://leocode.com/')
        return MainPage(self.driver)

    def __exit__(self, _type, _value, _tb):
        self.driver.quit()
