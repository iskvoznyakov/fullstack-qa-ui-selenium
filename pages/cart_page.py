from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.decorators import log_action


class CartPage(BasePage):
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(@id, 'remove')]")
    ITEM_NAME = (By.XPATH, "//div[@class = 'inventory_item_name']")
    ITEM_PRICE = (By.XPATH, "//div[@class = 'inventory_item_price']")

    @log_action
    def get_cart_items(self):
        return self.driver.find_elements(*self.ITEM_NAME)

    @log_action
    def get_number_of_cart_items(self):
        return len(self.driver.find_elements(*self.ITEM_NAME))

    @log_action
    def get_cart_prices(self):
        return self.driver.find_elements(*self.ITEM_PRICE)

    @log_action
    def proceed_to_checkout(self):
        return self.click(self.CHECKOUT_BUTTON)

    @log_action
    def continue_shopping(self):
        return self.click(self.CONTINUE_SHOPPING_BUTTON)
