from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from .locators import HomePageLocators
from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.url = HomePageLocators.URL_HOME
        self.browser.get(self.url)

    def go_to_login_page(self):
        self.click_element(HomePageLocators.LOGIN_LINK)

    def go_to_register_page(self):
        self.click_element(HomePageLocators.REGISTER_LINK)

    def click_filter_button_by_type(self):
        self.click_element(HomePageLocators.BUTTON_FILTER_BY_TYPE)

    def select_pet_by_type(self):
        self.find_element(HomePageLocators.SELECT_BY_TYPE)

    def click_fild_pet_name(self):
        self.click_element(HomePageLocators.FIELD_FILTER_BY_PET_NAME)

    def result_name_pet(self, text):
        search = self.find_element(HomePageLocators.FIELD_FILTER_BY_PET_NAME)
        search.send_keys(text)
        search.send_keys(Keys.ENTER)

    def check_filter_results(self, text):
        results = self.find_elements(HomePageLocators.FILTER_RESULT)
        for result in results:
            assert text in result.text, f"Text '{text}' not found in search results."

    def input_pet(self):
        self.result_name_pet('Ping')
        self.check_filter_results('Ping')
