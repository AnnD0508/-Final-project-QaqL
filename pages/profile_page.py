from .base_page import BasePage
from .locators import ProfilePageLocators
from selenium import webdriver


class ProfilePage(BasePage):

    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.url = ProfilePageLocators.URL_PROFILE
        self.browser.get(self.url)

    def profile_page_is_loaded(self):
        assert self.browser.current_url == self.url

    def count_pets(self):
        return len(self.find_elements(ProfilePageLocators.COUNT_PRPFILE_PETS))

    def click_button_add_pet(self):
        self.click_element(ProfilePageLocators.BUTTON_ADD_PET)

    def click_delete_button(self):
        return self.find_elements(ProfilePageLocators.BUTTON_DELETE)

    def deletion_confirmation(self):
        self.find_element(ProfilePageLocators.BUTTON_DELETION_CONFIRMATION).click()

    def remove_last_pet(self):
        pets = self.click_delete_button()
        pets[len(pets)-1].click()
        self.deletion_confirmation()

    def find_edit_button(self):
        return self.find_elements(ProfilePageLocators.BUTTON_EDIT)

    def edit_pet_button_click(self):
        pet_edit_buttons = self.find_edit_button()
        pet_edit_buttons[len(pet_edit_buttons) - 1].click()

    def go_from_profile_to_edit_page(self):
        assert self.get_text_from_element(ProfilePageLocators.EDIT_LINK) == "Edit pet's profile"

    def click_button_logo(self):
        self.click_element(ProfilePageLocators.HOME_LINK)

    def go_from_profile_to_home_page(self):
        assert self.get_title() == 'Vite App'

    def click_button_quit(self):
        self.click_element(ProfilePageLocators.BUTTON_QUIT)

    def go_from_profile_to_login_page(self):
        expected_url = 'http://34.141.58.52:8080/#/login'
        assert self.browser.current_url == expected_url
