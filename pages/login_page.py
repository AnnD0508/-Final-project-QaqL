from .base_page import BasePage
from .locators import LoginPageLocators, LoginData
from selenium import webdriver
import random
import string


class LoginPage(BasePage):
    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)
        self.url = LoginPageLocators.URL_LOGIN
        self.browser.get(self.url)

    def login_page_is_loaded(self):
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

    def input_email_unregistered_user(self):
        email = self.generate_email(10)
        self.send_keys(LoginPageLocators.FIELD_LOGIN_EMAIL, email)

    def input_password_unregistered_user(self):
        password = self.generate_password(9)
        self.send_keys(LoginPageLocators.FIELD_LOGIN_PASS, password)

    def message_for_unregistered_user(self):
        assert self.get_text_from_element(
            LoginPageLocators.MESSAGE_UNREGISTRED_DATE) == 'Something went wrong'

    def input_email_registered_user(self):
        login_email = self.find_element(LoginPageLocators.FIELD_LOGIN_EMAIL)
        login_email.send_keys(LoginData.EMAIL_AUTORIZATION)

    def input_password_registered_user(self):
        login_password = self.find_element(LoginPageLocators.FIELD_LOGIN_PASS)
        login_password.send_keys(LoginData. PASSWORD_AUTORIZATION)

    def button_submit(self):
        self.find_element(LoginPageLocators. LOGIN_BUTTON).submit()
