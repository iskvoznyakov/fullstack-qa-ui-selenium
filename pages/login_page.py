from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.decorators import log_action


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    @log_action
    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @log_action
    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)

    @log_action
    def get_error_text(self):
        return self.find(self.ERROR_MESSAGE).text
