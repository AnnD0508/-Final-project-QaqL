from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage


class TestHomePage:
    def test_go_to_login_page(self, browser):
        page = HomePage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login_page_is_loaded()

    def test_go_to_register_page(self, browser):
        page = HomePage(browser)
        page.open()
        page.go_to_login_page()
        registration_page = RegisterPage(browser)
        registration_page.open()
        registration_page.register_page_is_loaded()

    def test_pet_selection_by_type_and_name(self, browser):
        page = HomePage(browser)
        page.open()
        page.page_is_loaded()
        page.click_filter_button_by_type()
        page.select_pet_by_type()
        page.click_fild_pet_name()
        page.input_pet()
