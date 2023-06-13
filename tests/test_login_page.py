import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage


class TestLoginPage:

    @pytest.mark.smoke
    def test_input_date_registred_user(self, browser):
        home_page = HomePage(browser)
        home_page.open()
        home_page.page_is_loaded()
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login_page_is_loaded()
        login_page.input_email_registered_user()
        login_page.input_password_registered_user()
        login_page.button_submit()
        profile_page = ProfilePage(browser)
        profile_page.profile_page_is_loaded

    def test_input_data_unregistred_user(self, browser):
        home_page = HomePage(browser)
        home_page.open()
        home_page.page_is_loaded()
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login_page_is_loaded()
        login_page.input_email_unregistered_user()
        login_page.input_password_unregistered_user()
        login_page.button_submit()
        login_page.message_for_unregistered_user
