from selenium.webdriver.common.by import By


class HomePageLocators:
    URL_HOME = 'http://34.141.58.52:8080/#/'
    LOGIN_LINK = (By.XPATH,'//div//a[@href="#/login"]')
    REGISTER_LINK =(By.XPATH,'//div//a[@href="#/register"]')
    BUTTON_FILTER_BY_TYPE = (By.XPATH,'//div/span[@class="p-dropdown-trigger-icon pi pi-chevron-down"]')
    SELECT_BY_TYPE = (By.XPATH,'//ul/li[text()="cat"]')
    FIELD_FILTER_BY_PET_NAME = (By.XPATH, '//div/input[@class ="p-inputtext p-component w-full"]')
    FILTER_RESULT = (By.XPATH, '//div//div[text()="Ping"]')

class LoginPageLocators:
    URL_LOGIN = 'http://34.141.58.52:8080/#/login'
    FIELD_LOGIN_EMAIL = (By.XPATH, '//div/input[@class="p-inputtext p-component w-full"]')
    FIELD_LOGIN_PASS = (By.XPATH, '//div/input[@class="p-inputtext p-component"]')
    LOGIN_BUTTON = (By.XPATH, '//div//span[@class="p-button-label"]')
    MESSAGE_UNREGISTRED_DATE = (By.XPATH,'//div[@class="p-message-text" and text()="Something went wrong"]')


class LoginData:
    EMAIL_AUTORIZATION = 'annDqaq@mail.ru'
    PASSWORD_AUTORIZATION = '987654321'
    INCORRECT_EMAIL_AUTORIZATION = 'annDqaq@gmail.ru'
    INCORRECT_PASSWORD_AUTORIZATION = '123456789'


class RegisterPageLocators:
    URL_REGISTER = 'http://34.141.58.52:8080/#/register'
    FIELD_REGISTER_EMAIL = (By.XPATH, '//div/input[@class="p-inputtext p-component w-full"]')
    FIELD_REGISTER_PASS = (By.XPATH, '//div[@id="password"]//input')
    FIELD_REGISTER_CONFIRM_PASS = (By.XPATH, '//div[@id="confirm_password"]//input')
    SUBMIT_BUTTON = (By.XPATH,'//div//span[@class="p-hidden-accessible"]')
    CONFIRM_PASS_INCORRECT_MESSAGE  = (By.XPATH,'//div[@class="p-message-text" and text()="Something went wrong"]')
    EMAIL_INCORRECT_MESSAGE = (By.XPATH,'//div[text()="This field is email"]')
    FIELD_PASS_IS_EMPTY = (By.XPATH,'//div[text()="This field is required" ]')


class RegisterDaten:
    EMAIL_REGITRATION_CORRECT = 'exemple@yandex.ru'
    PASSWORD_REGISTRATION = '134679'
    PASSWORD_CONFIRMATION_CORRECT = '134679'
    PASSWORD_CONFIRMATION_INCORRECT = '124679'
    EMAIL_REGITRATION_INCORRECT = 'exempleyandex.ru'

class ProfilePageLocators:
    URL_PROFILE = 'http://34.141.58.52:8080/#/profile'
    BUTTON_ADD_PET = (By.XPATH,'//div/button[@class="p-button p-component p-button-icon-only p-button-rounded p-button-primary p-button-outlined"]')
    CREATE_LINK =  (By.XPATH, '//div[text()= "Create you pet profile"]')
    HOME_LINK = (By.XPATH,'//div/img[@class="logo mr-2"]')
    BUTTON_QUIT = (By.XPATH,'//div//li[@class="p-menuitem"][2]')
    COUNT_PRPFILE_PETS = (By.XPATH,'//div[@class="p-grid p-nogutter grid grid-nogutter"]/div')
    BUTTON_DELETE = (By.XPATH,'//div[@class="product-list-item"]//button[2]')
    BUTTON_DELETION_CONFIRMATION = (By.XPATH,'//div//button[@class="p-button p-component p-confirm-popup-accept p-button-sm"]')
    BUTTON_EDIT = (By.XPATH,'//div[@class="product-list-item"]//button[1]')
    EDIT_LINK = (By.XPATH,'//div[text()=" Edit pet\'s profile "]')

class PetProfilePageLocators:
    URL_NEW_PET = 'http://34.141.58.52:8080/#/pet-new/pet'
    FIELD_NAME = (By.XPATH, '//div/input[@id="name"]')
    BUTTON_SELECT_TYPE = (By.XPATH,'//div/span[@id="typeSelector"]')
    TYPE = (By.XPATH,'//ul/li[text()="reptile"]')
    FIELD_AGE = (By.XPATH,'//div//input[@class="p-inputtext p-component p-inputnumber-input"]')
    BUTTON_SELECT_GENDER = (By.XPATH,'//div[@id="pv_id_3"]//span[@aria-hidden="true"]')
    SELECT_GENDER = (By.XPATH,'//div//li[@id="pv_id_3_0"]')
    FIELD_NAME_IS_EMPTY_MESSAGE = (By.XPATH,'//div[text()="Name field is empty"]')
    FIELD_SELECT_TYPE_IS_EMPTY_MESSAGE = (By.XPATH,'//div[text()="This field is required"]')
    BUTTON_SUBMIT = (By.XPATH, '//div/button[@class="p-button p-component p-button-success"]')
    BUTTON_PROFILE_LINK = (By.XPATH, '//div//li/a[@href="#/profile"]')

    # MESSAGE_ABOUTE_ADD