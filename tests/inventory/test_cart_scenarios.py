import time

def test_add_item_to_cart_and_check_cart_badge(auth_inventory_page):
    auth_inventory_page.add_random_item_to_cart()

    assert auth_inventory_page.header.get_cart_badge_number() == 1

def test_add_item_to_cart_and_check_cart(auth_inventory_page, shopping_cart_page):
    auth_inventory_page.add_random_item_to_cart()
    auth_inventory_page.header.click_cart_button()

    assert auth_inventory_page.last_added_to_cart_item_name in shopping_cart_page.get_all_item_names_in_cart()
