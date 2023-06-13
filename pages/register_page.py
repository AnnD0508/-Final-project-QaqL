from .base_page import BasePage
from .locators import LoginPageLocators, LoginData
from .locators import RegisterPageLocators, RegisterDaten, ProfilePageLocators
from selenium import webdriver
import random
import string


class RegisterPage(BasePage):
    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.url = RegisterPageLocators.URL_REGISTER
        self.browser.get(self.url)

    def register_page_is_loaded(self):
        assert self.browser.current_url == self.url

    def generate_email(self, length=10):
        username = ''.join(random.choices(string.ascii_lowercase, k=length))
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "msn.com"]
        domain = random.choice(domains)
        email = f"{username}@{domain}"
        return email

    def generate_password(self, length=9):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        return password

    def input_correct_email_registration(self):
        email = self.generate_email(10)
        self.send_keys(RegisterPageLocators.FIELD_REGISTER_EMAIL, email)

    def input_correct_password_registration(self):
        password = RegisterDaten.PASSWORD_REGISTRATION
        self.send_keys(RegisterPageLocators.FIELD_REGISTER_PASS, password)

    def input_correct_confirmation_password_registration(self):
        confirmation_password = RegisterDaten.PASSWORD_CONFIRMATION_CORRECT
        self.send_keys(RegisterPageLocators.FIELD_REGISTER_CONFIRM_PASS, confirmation_password)

    def button_submit_registration(self):
        self.find_element(RegisterPageLocators.SUBMIT_BUTTON).submit()

    def registered_user_profile_is_loaded(self):
        assert self.browser.current_url == ProfilePageLocators.URL_PROFILE

    def input_incorrect_confirmation_password_registration(self):
        confirmation_password = RegisterDaten.PASSWORD_CONFIRMATION_INCORRECT
        self.send_keys(RegisterPageLocators.FIELD_REGISTER_CONFIRM_PASS, confirmation_password)

    def message_for_confirmation_password_registration(self):
        assert self.get_text_from_element(RegisterPageLocators.CONFIRM_PASS_INCORRECT_MESSAGE) == 'Something went wrong'

    def input_incorrect_email_registration(self):
        email = RegisterDaten. EMAIL_REGITRATION_INCORRECT
        self.send_keys(RegisterPageLocators.FIELD_REGISTER_EMAIL, email)

    def message_input_incorrect_email_registration(self):
        assert self.get_text_from_element(RegisterPageLocators.EMAIL_INCORRECT_MESSAGE) == 'This field is email'

    def message_password_registration_is_empty(self):
        assert self.get_text_from_element(RegisterPageLocators.FIELD_PASS_IS_EMPTY) == 'This field is required'

    def input_password_registered_user(self):
        login_password = self.find_element(LoginPageLocators.FIELD_LOGIN_PASS)
        login_password.send_keys(LoginData.PASSWORD_AUTORIZATION)
