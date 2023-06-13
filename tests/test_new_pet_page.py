from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.new_pet_profile_page import NewPetPage
import time


class TestNewPetPage:

    def test_add_new_pet(self, browser):
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
        count_pets_before = profile_page.count_pets()
        profile_page.click_button_add_pet()
        create_pet_page = NewPetPage(browser)
        create_pet_page.create_pet_profile_is_loaded()
        time.sleep(3)
        create_pet_page.input_field_new_name_pet()
        create_pet_page.select_type_new_pet()
        create_pet_page.input_field_age_new_pet()
        create_pet_page.select_gender_new_pet()
        create_pet_page.submit_create()
        create_pet_page.go_from_created_pet_to_profile()
        profile_page = ProfilePage(browser)
        profile_page.open()
        time.sleep(10)
        profile_page.profile_page_is_loaded()
        count_pets_after = profile_page.count_pets()
        assert (count_pets_before + 1 == count_pets_after)
