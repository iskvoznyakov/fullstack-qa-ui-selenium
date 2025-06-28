import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import BASE_URL
from pages.login_page import LoginPage
import allure


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # Получаем результат выполнения теста
    outcome = yield
    rep = outcome.get_result()

    # Проверяем: если тест "упал" на этапе вызова
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Прикрепляем скриншот
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            # Прикрепляем HTML страницы
            allure.attach(
                driver.page_source,
                name="Page Source",
                attachment_type=allure.attachment_type.HTML
            )
