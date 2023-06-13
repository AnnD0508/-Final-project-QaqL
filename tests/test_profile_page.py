from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
import time


class TestProfilePage:

    def test_remove_pet(self, browser):
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
        profile_page.open()
        time.sleep(3)
        profile_page.profile_page_is_loaded()
        count_pets_before = profile_page.count_pets()
        profile_page.remove_last_pet()
        profile_page.open()
        time.sleep(3)
        count_pets_after = profile_page.count_pets()
        assert (count_pets_before - 1 == count_pets_after)

    def test_back_from_profile_to_home_page(self, browser):
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
        time.sleep(3)
        profile_page.profile_page_is_loaded()
        profile_page.click_button_logo()
        profile_page.go_from_profile_to_home_page()

    def test_go_from_profile_to_edite_page(self, browser):
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
        profile_page.open()
        time.sleep(5)
        profile_page.profile_page_is_loaded()
        profile_page.edit_pet_button_click()
        profile_page.go_from_profile_to_edit_page()

    def test_back_from_profile_to_login_page(self, browser):
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
        profile_page.open()
        time.sleep(5)
        profile_page.profile_page_is_loaded()
        profile_page.click_button_quit()
        time.sleep(5)
        profile_page.go_from_profile_to_login_page()
