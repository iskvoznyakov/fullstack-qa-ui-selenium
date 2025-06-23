import pytest
from pages.inventory_page import InventoryPage


def test_inventory_items_visible_after_login(logged_in_driver):
    inventory_page = InventoryPage(driver=logged_in_driver)
    assert inventory_page.cart_icon_is_visible(), f'Иконка корзины не отображается'
    assert inventory_page.get_number_of_inventory_items() > 0, f'Не найдено товаров'


@pytest.mark.parametrize("sorting_option, expected_order", [
    ("Name (A to Z)", sorted),
    ("Name (Z to A)", lambda items: sorted(items, reverse=True))
])
def test_sorting_by_name(logged_in_driver, sorting_option, expected_order):
    inventory_page = InventoryPage(driver=logged_in_driver)
    inventory_page.apply_sorting(visible_text=sorting_option)
    items_names = inventory_page.get_all_item_names()
    assert items_names == expected_order(items_names), f"Сортировка {sorting_option} работает некорректно"

# TODO разобраться со всплывающим окном "Смените пароль"
# def test_add_one_item_to_cart(logged_in_driver):
#     inventory_page = InventoryPage(driver=logged_in_driver)
#     item_name = inventory_page.get_information_about_item_by_order(1)["Name"]
#     inventory_page.click_add_to_cart_for(item_name)
#     assert inventory_page.get_number_of_items_in_cart() == 1, f"Товар '{item_name}' не добавлен в корзину"
