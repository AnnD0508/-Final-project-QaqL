from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.register_page import RegisterPage
import time
import pytest


@pytest.mark.xfail(reason="This test is expected to fail - bug found")
class TestRegisterPage:

    def test_input_correct_data_registration_new_user(self, browser):
        home_page = HomePage(browser)
        home_page.open()
        home_page.page_is_loaded()
        registration_page = RegisterPage(browser)
        registration_page.open()
        registration_page.register_page_is_loaded()
        registration_page.input_correct_email_registration()
        registration_page.input_correct_password_registration()
        registration_page.input_correct_confirmation_password_registration()
        registration_page.button_submit_registration()
        profile_page = ProfilePage(browser)
        profile_page.open()
        time.sleep(5)
        profile_page.profile_page_is_loaded()

    def test_input_incorrect_data_confirmation_pass_registration(self, browser):
        home_page = HomePage(browser)
        home_page.open()
        home_page.page_is_loaded()
        registration_page = RegisterPage(browser)
        registration_page.open()
        registration_page.register_page_is_loaded()
        registration_page.input_correct_email_registration()
        registration_page.input_correct_password_registration()
        registration_page.input_incorrect_confirmation_password_registration()
        registration_page.button_submit_registration()
        registration_page. message_for_confirmation_password_registration()

    def test_input_incorrect_data_email_registration(self, browser):
        home_page = HomePage(browser)
        home_page.open()
        home_page.page_is_loaded()
        registration_page = RegisterPage(browser)
        registration_page.open()
        registration_page.register_page_is_loaded()
        registration_page.input_incorrect_email_registration()
        registration_page.input_correct_password_registration()
        registration_page.input_correct_confirmation_password_registration()
        registration_page.button_submit_registration()
        registration_page.message_input_incorrect_email_registration()

    def test_field_password_registration_is_empty(self, browser):
        home_page = HomePage(browser)
        home_page.open()
        home_page.page_is_loaded()
        registration_page = RegisterPage(browser)
        registration_page.open()
        registration_page.register_page_is_loaded()
        registration_page.input_correct_email_registration()
        registration_page.input_correct_confirmation_password_registration()
        registration_page.button_submit_registration()
        registration_page.message_password_registration_is_empty()
