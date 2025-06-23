import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import BASE_URL
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.login("standard_user", "secret_sauce")

    yield driver
