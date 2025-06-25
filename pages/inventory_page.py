from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.decorators import log_action


class InventoryPage(BasePage):
    SHOPPING_CART_ICON = (By.ID, "shopping_cart_container")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    FILTER_DROPDOWN_LIST = (By.XPATH, "//select[@data-test='product-sort-container']")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    INVENTORY_NAME = (By.XPATH, "//div[@data-test='inventory-item-name']")
    INVENTORY_DESCRIPTION = (By.XPATH, "//div[@data-test='inventory-item-desc']")
    INVENTORY_PRICE = (By.XPATH, "//div[@data-test='inventory-item-price']")

    @log_action
    def get_number_of_inventory_items(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEM))

    @log_action
    def _get_all_the_inventory_items(self):
        return self.driver.find_elements(*self.INVENTORY_ITEM)

    @log_action
    def cart_icon_is_visible(self):
        return self.is_visible(self.SHOPPING_CART_ICON)

    @log_action
    def click_add_to_cart_for(self, item_name: str):
        for item in self._get_all_the_inventory_items():
            name = item.find_element(*self.INVENTORY_NAME).text.strip()
            if name == item_name.strip():
                add_button = item.find_element(By.TAG_NAME, "button")
                add_button.click()
                return
        raise ValueError(f"Товар с именем '{item_name}' не найден на странице")

    @log_action
    def get_number_of_items_in_cart(self):
        icon = self.find(self.SHOPPING_CART_BADGE)
        return int(icon.text) if icon.text else 0

    @log_action
    def get_information_about_item_by_order(self, order: int):
        item = self._get_all_the_inventory_items()[order - 1]
        return {
            "Name": item.find_element(*self.INVENTORY_NAME).text,
            "Description": item.find_element(*self.INVENTORY_DESCRIPTION).text,
            "Price": item.find_element(*self.INVENTORY_PRICE).text
        }

    @log_action
    def apply_sorting(self, visible_text: str):
        dropdown = Select(self.find(self.FILTER_DROPDOWN_LIST))
        dropdown.select_by_visible_text(visible_text)

    @log_action
    def get_all_item_names(self) -> list[str]:
        return [item.find_element(*self.INVENTORY_NAME).text for item in self._get_all_the_inventory_items()]
