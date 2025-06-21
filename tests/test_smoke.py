from config.config import BASE_URL
from pages.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver=driver)
    login_page.open(BASE_URL)
    login_page.login(username="standard_user", password="secret_sauce")
    assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html",\
        f"После попытки залогиниться - url страницы: {login_page.driver.current_url}"
