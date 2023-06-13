from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

        def __init__(self, browser: webdriver.Chrome):
            self.browser = browser
            self.url: str = ''

        def open_url(self, url):
            self.browser.get(url)

        def open(self):
            self.open_url(url=self.url)

        def page_is_loaded(self):
            assert self.browser.current_url == self.url

        def find_element(self, locator, timer=10):
            return WebDriverWait(self.browser, timer).until(
                EC.presence_of_element_located(locator))

        def find_elements(self, locator, timer=10):
            return WebDriverWait(self.browser, timer).until(
                EC.presence_of_all_elements_located(locator))

        def click_element(self, locator, timer=10):
            return WebDriverWait(self.browser, timer).until(
                EC.element_to_be_clickable(locator)).click()

        def send_keys(self, locator, content, timer=10):
            input_field = WebDriverWait(self.browser, timer).until(
                EC.element_to_be_clickable(locator))
            input_field.clear()
            input_field.send_keys(content)

        def get_text_from_element(self, locator, timer=10):
            element = self.find_element(locator, timer)
            return element.text

        def get_title(self):
            return self.browser.title
