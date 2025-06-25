from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, 1)

    def open(self, url):
        logger.info(f"Переход на страницу: {url}")
        self.driver.get(url)

    def find(self, locator):
        logger.info(f"Поиск элемента: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator), f"There's no element: {locator}")

    def click(self, locator):
        logger.info(f"Клик по элементу: {locator}")
        self.find(locator).click()

    def enter_text(self, locator, text):
        logger.info(f"Ввод '{text}' в: {locator}")
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    def is_visible(self, locator):
        logger.info(f"Проверка видимости {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        logger.info(f"Получение текста из {locator}")
        return self.find(locator).text
