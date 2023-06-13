import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
