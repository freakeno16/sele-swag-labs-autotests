import time


def test_add_item_to_cart(auth_inventory_page, shopping_cart_page):
    auth_inventory_page.add_random_item_to_cart()
    auth_inventory_page.header.click_cart_button()
    assert auth_inventory_page.last_added_to_cart_item_name in shopping_cart_page.get_all_item_names_in_cart()
