from .base_page import BasePage
from .locators import PetProfilePageLocators
from selenium import webdriver


class NewPetPage(BasePage):
    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.url = PetProfilePageLocators.URL_NEW_PET
        self.browser.get(self.url)

    def create_pet_profile_is_loaded(self):
        assert self.browser.current_url == self.url

    def input_field_new_name_pet(self):
        new_name = 'ILONMASK'
        self.send_keys(PetProfilePageLocators.FIELD_NAME, new_name)

    def select_type_new_pet(self):
        self.find_element(PetProfilePageLocators.BUTTON_SELECT_TYPE).click()
        type_pet = self.find_element(PetProfilePageLocators.TYPE)
        type_pet.click()

    def input_field_age_new_pet(self):
        age = '45'
        self.send_keys(PetProfilePageLocators.FIELD_AGE, age)

    def select_gender_new_pet(self):
        self.click_element(PetProfilePageLocators.BUTTON_SELECT_GENDER)
        gender_pet = self.find_element(PetProfilePageLocators.SELECT_GENDER)
        gender_pet.click()

    def submit_create(self):
        self.click_element(PetProfilePageLocators.BUTTON_SUBMIT)

    def go_from_created_pet_to_profile(self):
        self.click_element(PetProfilePageLocators.BUTTON_PROFILE_LINK)
