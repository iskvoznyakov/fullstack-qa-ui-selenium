import pytest
from config.config import BASE_URL
from pages.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver=driver)
    login_page.open(BASE_URL)
    login_page.login(username="standard_user", password="secret_sauce")
    assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html", \
        f"После попытки залогиниться - url страницы: {login_page.driver.current_url}"


@pytest.mark.parametrize("username, password, error_message", [
    ("", "", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("not_standard_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "not_secret_sauce", "Epic sadface: Username and password do not match any user in this service")
], ids=[
    "Username and password are empty",
    "Valid username and empty password",
    "Empty username and valid password",
    "Invalid username and valid password",
    "Valid username and invalid password"
])
def test_failed_login(driver, username, password, error_message):
    login_page = LoginPage(driver=driver)
    login_page.open(BASE_URL)
    login_page.login(username=username, password=password)
    assert login_page.is_error_displayed(), f"Сообщение об ошибки не отображается"
    actual_error_message = login_page.get_error_text()
    assert actual_error_message == error_message, \
        f"Сообщение об ошибке не совпадает. Отображается {actual_error_message}"
