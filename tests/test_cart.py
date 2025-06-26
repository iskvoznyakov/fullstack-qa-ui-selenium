from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
import allure


@allure.feature("Корзина товаров")
@allure.story("Добавление товаров в корзину")
@allure.title("Проверка добавление товаров в корзину")
@allure.description("Тест проверяет, что в корзине отображается добавленный товар")
def test_item_is_added_to_cart(logged_in_driver):
    with allure.step("Инициализируем InventoryPage"):
        inventory_page = InventoryPage(driver=logged_in_driver)
    with allure.step("Добавляем 1 товар в корзину"):
        item_name = inventory_page.get_information_about_item_by_order(1)["Name"]
        inventory_page.click_add_to_cart_for(item_name)
    with allure.step("Открываем корзину"):
        inventory_page.open_cart()
    with allure.step("Инициализируем CartPage"):
        cart_page = CartPage(driver=logged_in_driver)
    with allure.step("Проверяем количество товаров в корзине"):
        number_of_cart_items = cart_page.get_number_of_cart_items()
        assert number_of_cart_items == 1, f'Количество товаров в корзине не 1, а {number_of_cart_items}'
